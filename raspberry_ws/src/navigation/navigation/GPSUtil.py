import folium
from folium.plugins import MeasureControl, Geocoder
from geopy.distance import geodesic
import geopy
import threading

#TODO: make self.trajectory to self.main_trajectory.
# use self.main_trajectory to save the starting and ending point.
# create variable called self.perpendicullar_trajectory ( used for
# the red line being the trajectory that appears when the boat strays off
# course and points to the main_trajectory. Create variable called self.current_trajectory
# make the program switch the current_trajectory between main_trajectory and
# perpendicullar_trajectory. The aim is to make the boat follow the red one to get back on course.

# TODO: make the current location a boat marker and add compass to know where the hull is heading
class GPSUtil:
    # singleton class pattern
    __instance = None
    __lock = threading.Lock()
    def __new__(cls, *args, **kwargs):
        with cls.__lock:
            if cls.__instance is None:
                cls.__instance = super(GPSUtil, cls).__new__(cls)
                cls.__instance._initialized = False
        return cls.__instance
    @classmethod
    def get_instance(cls, current_location=None, frame=None):
        instance = cls(current_location, frame)
        return instance
    def __init__(self, current_location=None, frame=None):
        if self._initialized:
            return
        self._initialized = True

        self.current_location = current_location or (0.0, 0.0)
        self.mymap = folium.Map(location=self.current_location, zoom_start=17)
        self.mymap.add_child(MeasureControl())
        self.mymap.add_child(Geocoder())

        self.left_boundary = (42.727850, 27.608618)
        self.right_boundary = (42.725266, 27.612694)
        self.top_boundary = (42.722352, 27.608125)
        self.bottom_boundary = (42.725343, 27.602592)

        self.frame = frame or [self.left_boundary, self.right_boundary, self.top_boundary, self.bottom_boundary]
        self.update_frame(self.frame)

        self.start = self.current_location
        self.destination = (10, 10)  # Here self.destination is assigned a value
        self.adjust_trajectory_to_boundary()
        self.trajectory = folium.PolyLine(locations=[self.start, self.destination], color='blue', popup="Trajectory")

# POINTS, LINES AND DISTANCE
    def distance_between(self, point1, point2):
        """Calculate the difference between two points (GPS coordinates)
        and returns the difference in meters."""

        print(f"[GPSUTIL](distance between)point1: {point1}, point2: {point2}")
        return geodesic(point1, point2).meters

# TODO: compare thew two functions
    def distance_point_to_line(self, point, start, end):
        """Returns the perpendicular distance  between point and a given line.

               Parameters
               ----------
               point : gps point( longitude, latitude)
                   Defines the location from which to measure
               start : gps point( longitude, latitude)
                    Defines the starting point of the line
               end : gps point( longitude, latitude)
                   Defines the ending point of the line
        """

        x, y = point
        x1, y1 = start
        x2, y2 = end

        numerator = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1)
        denominator = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

        return numerator / denominator

    def distance_point_to_line_closest(self, point, start, end):
        """Returns the closest distance between point and a given line (segment).

                       Parameters
                       ----------
                       point : gps point( longitude, latitude)
                           Defines the location from which to measure
                       start : gps point( longitude, latitude)
                            Defines the starting point of the line
                       end : gps point( longitude, latitude)
                           Defines the ending point of the line
                """
        x, y = point
        x1, y1 = start
        x2, y2 = end

        # Vector AB - the vector from the start to the end of line
        ABx = x2 - x1
        ABy = y2 - y1

        # Vector AP - - the vector from the start of the line to the point
        APx = x - x1
        APy = y - y1

        # Vector BP - the vector from the end of the line to the point
        BPx = x - x2
        BPy = y - y2

        # Dot product of AP and AB
        dot_product = APx * ABx + APy * ABy

        # Length of AB squared
        len_AB_squared = ABx * ABx + ABy * ABy

        # Parameter t to determine the closest point on the line segment
        t = dot_product / len_AB_squared

        # there are two possible options from here on. first is if the point
        # is next to the line and the second is when the point is above or
        # below the line

        # Closest point falls within the segment
        if 0 <= t <= 1:
            closest_x = x1 + t * ABx
            closest_y = y1 + t * ABy
            distance = math.sqrt((closest_x - x) ** 2 + (closest_y - y) ** 2)
        else:
            # Closest point falls outside the segment, closer to one of the endpoints
            # Calculate distance to both endpoints and return the smaller one
            dist_to_start = math.sqrt(APx ** 2 + APy ** 2)
            dist_to_end = math.sqrt(BPx ** 2 + BPy ** 2)
            distance = min(dist_to_start, dist_to_end)

        return distance

    def point_position_relative_to_line(self, line=None, point=None):
        """returns the position of a provided point (str - left/right)
         relative to a provided line/trajectory (an array of two gps points).
         calculated by using cross product.

               If the argument `line` isn't passed in, it is automatically assigned the
               value of self.trajectory .

               If the argument `point` isn't passed in, it is automatically assigned the
               value of self.current_location .

               Parameters
               ----------
               line : list( beginning gps point, ending gps point), optional
                   Defines the line that the point is compared to
               point : gps point( longitude, latitude), optional
                   Defines the point

               Raises
               ------

               """
        if not line:
            line = self.trajectory

        start = line.locations[0]
        end = line.locations[1]
        if not point:
            point = self.current_location

        cross = self.cross_product(start, end, point)
        if cross > 0:
            return "left"
        elif cross < 0:
            return "right"
        else:
            return "forward"  # on the line

    def cross_product(self, p1, p2, p3):
        """Returns the cross product between three points"""

        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    def update_current_location(self, point):
        self.current_location = point

# FRAME
    def update_frame(self, frame):
        """Changes frame points on the map
               Parameters
               ----------
               frame : list of 4 gps coordinates
                   top left, top right, bottom right, bottom left
               """

        top_left, top_right, bottom_right, bottom_left = frame
        self.frame = {
            "Top": (top_left, top_right),
            "Right": (top_right, bottom_right),
            "Bottom": (bottom_right, bottom_left),
            "Left": (bottom_left, top_left)
        }
        self.top_boundary = folium.PolyLine(locations=[top_left, top_right], color='green', popup="Top Boundary")
        self.right_boundary = folium.PolyLine(locations=[top_right, bottom_right], color='green', popup="Right Boundary")
        self.bottom_boundary = folium.PolyLine(locations=[bottom_right, bottom_left], color='green', popup="Bottom Boundary")
        self.left_boundary = folium.PolyLine(locations=[bottom_left, top_left], color='green', popup="Left Boundary")
    def is_inside_frame(self):
        """Returns a boolean value indicating if current location is inside the given frame"""

        sides = (self.left_boundary, self.bottom_boundary, self.right_boundary, self.top_boundary)
        for side in sides:
            point_on_side = str(self.point_position_relative_to_line(line=side)).lower()
            if point_on_side == "left":
                pass
            else:
                return False
        return True
    def assign_points_on_boundaries_of_frame(self, interval_meters):
        # TODO: make it work only on upper and lower boundary and assign numbers to
        #  all the points, so that they can be put in a list and poped once gone through.

        """Splits the map on points. These points are used by the
        boat to go through one by one

               Parameters
               ----------
               interval_meters : integer representing the distance between the points
                    in meters

                       """

        if not self.frame or len(self.frame) == 0:
            return

        for side, boundary_points in self.frame.items():
            if len(boundary_points) != 2:
                continue

            start_point, end_point = boundary_points
            total_distance = self.distance_between(start_point, end_point)
            num_points = int(total_distance / interval_meters)
            for i in range(1, num_points + 1):
                ratio = i / (num_points + 1)
                new_point = (
                    start_point[0] + ratio * (end_point[0] - start_point[0]),
                    start_point[1] + ratio * (end_point[1] - start_point[1])
                )
                label = f"point_{side}_{i}"
                marker = folium.Marker(location=new_point, popup=label, color="purple")
                marker.add_to(self.mymap)
                point_name = f"{side}_{i}"
                setattr(self, point_name, new_point)


# DESTINATION
    def has_reached_destination(self):
        """Returns a boolean that represents whether the boat
        has reached its current destination point
        """

        distance_to_destination = self.distance_between(self.current_location, self.destination)
        print(f"[GPS_UTIL] distance to destination: {distance_to_destination}")
        return distance_to_destination <= 5

    # TODO: as the code is using east and west to move the destination
    #  I need to make sure that it works no matter how the frame is
    #  orientated.

    # TODO: make sure that the destination is changing upon arrival to the new one

    # TODO: make sure that the new destination is on the opposite side of the frame


    def move_destination_to_right(self, distance_meters=10):
        """Moves the current destination point to the right

               Parameters
               ----------
               distance_meters : integer representing the distance between the
                    curremt destination and the new one in meters"""

        if not self.current_location:
            return None

        bearing = 90  # 90 degrees represents moving eastwards (to the right)
        new_destination = geopy.distance.distance(meters=distance_meters).destination(self.current_location, bearing)
        self.destination = new_destination
    def move_destination_to_left(self, distance_meters=10):
        """Moves the current destination point to the right

                       Parameters
                       ----------
                       distance_meters : integer representing the distance between the
                            curremt destination and the new one in meters"""

        if not self.current_location:
            return None

        bearing = 270  # 270 degrees represents moving westwards (to the left)
        new_destination = geopy.distance.distance(meters=distance_meters).destination(self.current_location, bearing)
        self.destination = new_destination

# TRAJECTORY
    def adjust_trajectory_to_boundary(self):
        """Moves the current destination point to upper boundary
        when boat has reached its destination on the lower boundary
        or it moves it to the lower boundary when boat has
        reached upper boundary
        """

        #ensure that all required parameters have assigned values
        if not self.current_location or not self.frame or len(self.frame) == 0:
            return

        top_boundary = self.frame.get("Top", ())[0]
        bottom_boundary = self.frame.get("Bottom", ())[0]

        if not top_boundary or not bottom_boundary:
            return
        # calculate the distance from the current location to both
        # boundaries. This way it is known which one is closer and which
        # one should be reached next
        distance_to_top = self.distance_between(self.current_location, top_boundary)
        distance_to_bottom = self.distance_between(self.current_location, bottom_boundary)

        if distance_to_top < distance_to_bottom:
            self.update_trajectory(self.current_location, self.closest_point_on_trajectory(trajectory=self.bottom_boundary))
        else:
            self.update_trajectory(self.current_location, self.closest_point_on_trajectory(trajectory=self.top_boundary))

    # TODO: find the difference between this "closest_point_on_trajectory"
    #  function and "distance_point_to_line_closest"
    def closest_point_on_trajectory(self, trajectory=None):
        """Returns the closest point to a given line (segment) relative to current location.

           Parameters
           ----------
           trajectory : list of two gps points, optional
               Default value is current_trajectory

                        """
        point = self.current_location

        if not trajectory:
            trajectory = self.trajectory
            start = self.start
            destination = self.destination
        else:
            trajectory = trajectory
            start = trajectory.locations[0]
            destination = trajectory.locations[1]

        if not trajectory:
            return None

        x0, y0 = point
        x1, y1 = start
        x2, y2 = destination

        dx = x2 - x1
        dy = y2 - y1

        if dx == 0 and dy == 0:
            return start

        t = ((x0 - x1) * dx + (y0 - y1) * dy) / (dx ** 2 + dy ** 2)

        if t < 0:
            return start
        elif t > 1:
            return destination
        else:
            x = x1 + t * dx
            y = y1 + t * dy
            return x, y



    def update_trajectory(self, start, destination):
        """changes the current_trajectory value.

           Parameters
           ----------
           start : gps point( longitude, latitude)
               Defines the location from which to start the trajectory
           destination : gps point( longitude, latitude)
                Defines the end of trajectory

                        """

        self.start = start
        self.destination = destination
        self.trajectory = folium.PolyLine(locations=[start, destination], color='blue', popup="Trajectory")
    def distance_to_trajectory(self):
        "Returns the distance between the current location and the current destination in meters"

        point = self.current_location
        if self.trajectory:
            closest_point = self.closest_point_on_trajectory()
            distance = self.distance_between(point, closest_point)

            # Determine if the point is on the left or right side of the trajectory
            cross_product = (point[0] - closest_point[0]) * (self.destination[1] - closest_point[1]) - \
                            (point[1] - closest_point[1]) * (self.destination[0] - closest_point[0])

            if cross_product > 0:
                side = 'Right'
            elif cross_product < 0:
                side = 'Left'
            else:
                side = 'On the Trajectory'

            return distance, side
        else:
            return None, None

    # VISUALIZATION
    def plot_trajectory(self):
        "plots the trajectory on the map (self.mymap)"
        map_center = self.current_location

        points = {
            "Starting Point": self.start,
            "Destination Point": self.destination,
            "Current Location": self.current_location,
        }

        for label, point in points.items():
            if point:
                marker = folium.Marker(location=point, popup=label)
                marker.add_to(self.mymap)

        if self.trajectory:
            self.trajectory.add_to(self.mymap)

    def plot_map(self, name="map"):
        "Generates html file that visualizes all the points and maps on the map"

        self.mymap = folium.Map(location=self.current_location, zoom_start=20)
        self.plot_trajectory()

        if self.frame and len(self.frame) == 4:
            for connection_name, connection_points in self.frame.items():
                connection = folium.PolyLine(locations=connection_points, color='green', popup=connection_name)
                connection.add_to(self.mymap)

        if self.top_boundary:
            self.top_boundary.add_to(self.mymap)
        if self.right_boundary:
            self.right_boundary.add_to(self.mymap)
        if self.bottom_boundary:
            self.bottom_boundary.add_to(self.mymap)
        if self.left_boundary:
            self.left_boundary.add_to(self.mymap)

        if self.current_location:
            closest_point_on_trajectory = self.closest_point_on_trajectory()
            distance_line = folium.PolyLine(locations=[self.current_location, closest_point_on_trajectory], color='red', popup="Distance to Trajectory")
            distance_line.add_to(self.mymap)

        self.mymap.save(f"{name}.html")