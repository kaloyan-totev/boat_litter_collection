import folium
from folium.plugins import MeasureControl
from folium.plugins import Geocoder
from geopy.distance import geodesic

class GPSUtil:
    def __init__(self, current_location, frame):

        self.current_location = current_location
        self.mymap = folium.Map(location=self.current_location, zoom_start=17)
        self.mymap.add_child(MeasureControl())
        self.mymap.add_child(Geocoder())

        self.left_boundary = None
        self.right_boundary = None
        self.top_boundary = None
        self.bottom_boundary = None
        self.frame = frame
        self.update_frame(frame)

        self.start = current_location
        self.destination = None
        # here self.destination is assigned a value
        self.adjust_trajectory_to_boundary()
        self.trajectory = folium.PolyLine(locations=[self.start, self.destination], color='blue', popup="Trajectory")

    def distance_between(self, point1, point2):
        # Calculate the difference between two points (gps coordinates)
        return geodesic(point1, point2).meters

    def distance_to_trajectory(self):
        point = self.current_location
        """
        Calculate the distance between a point and the trajectory,
        and determine if the point is on the left or right of the trajectory.

        Args:
            point (tuple): GPS coordinates (latitude, longitude) of the point.

        Returns:
            tuple: A tuple containing the distance to the trajectory and
                   a string indicating whether the point is on the left or right side.
        """
        if self.trajectory:
            closest_point = self.closest_point_on_trajectory(line)
            distance = self.distance_between(point, closest_point)

            # Determine if the point is on the left or right side of the trajectory
            # Calculate the cross product of vectors from the current point to the closest point
            # and from the current point to the next point on the trajectory
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

    def point_position_relative_to_line(self, line=None, point=None):
        if(line==None):
            line = self.trajectory

        start = line.locations[0]
        end = line.locations[1]
        if(not point):
            point = self.current_location

        """
        Determine the position of a point relative to a line defined by two points.

        Args:
            point (tuple): GPS coordinates (latitude, longitude) of the point.
            start (tuple): GPS coordinates of the line's starting point.
            end (tuple): GPS coordinates of the line's ending point.

        Returns:
            str: A string indicating whether the point is on the left, right, or on the line.
        """
        cross = self.cross_product(start, end, point)
        if cross > 0:
            return "Left"
        elif cross < 0:
            return "Right"
        else:
            return "On the line"

    def distance_point_to_line(self, point, start, end):
        """
        Calculate the perpendicular distance from a point to a line defined by two points.

        Args:
            point (tuple): GPS coordinates (latitude, longitude) of the point.
            start (tuple): GPS coordinates of the line's starting point.
            end (tuple): GPS coordinates of the line's ending point.

        Returns:
            float: The perpendicular distance from the point to the line in meters.
        """
        x, y = point
        x1, y1 = start
        x2, y2 = end

        numerator = abs((y2 - y1) * x - (x2 - x1) * y + x2 * y1 - y2 * x1)
        denominator = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5

        return numerator / denominator

    def cross_product(self, p1, p2, p3):
        """
        Calculate the cross product of vectors formed by three points.

        Args:
            p1 (tuple): GPS coordinates of the first point.
            p2 (tuple): GPS coordinates of the second point.
            p3 (tuple): GPS coordinates of the third point.

        Returns:
            float: The cross product of the vectors formed by the three points.
        """
        return (p2[0] - p1[0]) * (p3[1] - p1[1]) - (p2[1] - p1[1]) * (p3[0] - p1[0])

    def update_trajectory(self, start, destination):
        # Update the trajectory between two points
        self.start = start
        self.destination = destination
        self.trajectory = folium.PolyLine(locations=[start, destination], color='blue', popup="Trajectory")

    def update_current_location(self, point):
        # Update the current location
        self.current_location = point

    def update_frame(self, frame):
        top_left, top_right, bottom_right, bottom_left = frame
        # Update the frame points
        self.frame = {
            "Top": (top_left, top_right),
            "Right": (top_right, bottom_right),
            "Bottom": (bottom_right, bottom_left),
            "Left": (bottom_left, top_left)
        }
        # Update separate fields for each boundary
        self.top_boundary = folium.PolyLine(locations=[top_left, top_right], color='green', popup="Top Boundary")
        self.right_boundary = folium.PolyLine(locations=[top_right, bottom_right], color='green', popup="Right Boundary")
        self.bottom_boundary = folium.PolyLine(locations=[bottom_right, bottom_left], color='green', popup="Bottom Boundary")
        self.left_boundary = folium.PolyLine(locations=[bottom_left, top_left], color='green', popup="Left Boundary")

    def visualize_trajectory(self):
        # Create a map centered at the start coordinate
        map_center = self.current_location


        # Add markers for start, destination, and current location
        points = {
            "Starting Point": self.start,
            "Destination Point": self.destination,
            "Current Location": self.current_location,
        }

        for label, point in points.items():
            if point:
                marker = folium.Marker(location=point, popup=label)
                marker.add_to(self.mymap)

        # Add PolyLine for the trajectory (in blue)
        if self.trajectory:
            self.trajectory.add_to(self.mymap)

        # Save the map as an HTML file
        self.mymap.save("trajectory_map.html")

    def plot_map(self,name="map"):
        # Create a map centered at the start coordinate
        self.visualize_trajectory()

        # Plot connections between frame points with labels in green
        if self.frame and len(self.frame) == 4:
            for connection_name, connection_points in self.frame.items():
                connection = folium.PolyLine(locations=connection_points, color='green', popup=connection_name)
                connection.add_to(self.mymap)

        # Plot separate boundaries in green
        if self.top_boundary:
            self.top_boundary.add_to(self.mymap)
        if self.right_boundary:
            self.right_boundary.add_to(self.mymap)
        if self.bottom_boundary:
            self.bottom_boundary.add_to(self.mymap)
        if self.left_boundary:
            self.left_boundary.add_to(self.mymap)

        # Plot the distance line between current location and trajectory in red
        if self.current_location:
            closest_point_on_trajectory = self.closest_point_on_trajectory()
            distance_line = folium.PolyLine(locations=[self.current_location, closest_point_on_trajectory],
                                           color='red', popup="Distance to Trajectory")
            distance_line.add_to(self.mymap)

        # Save the map as an HTML file

        self.mymap.save(f"{name}.html")

    def has_reached_destination(self):
        distance_to_destiantion = self.distance_between(self.current_location,self.destination)
        # units are in meters
        return distance_to_destiantion<=5

    def move_destination_to_right(self,distance_meters = 10):
        if not self.current_location:
            return None

        # Define the direction and distance to move in meters
        bearing = 90  # 90 degrees represents moving eastwards (to the right)

        # Calculate the destination point using geopy
        new_destination = geopy.distance.distance(meters=distance_meters).destination(self.current_location, bearing)
        self.destination = new_destination
    def move_destination_to_left(self,distance_meters = 10):
        if not self.current_location:
            return None

        # Define the direction and distance to move in meters
        bearing = 270  # 270 degrees represents moving westwards (to the left)


        # Calculate the destination point using geopy
        new_destination = geopy.distance.distance(meters=distance_meters).destination(self.current_location, bearing)
        self.destination = new_destination
    def adjust_trajectory_to_boundary(self):
            """
            Adjusts the trajectory based on the current location's proximity to the top or bottom boundary.
            """
            if not self.current_location or not self.frame or len(self.frame) == 0:
                return

            top_boundary = self.frame.get("Top", ())[0]
            bottom_boundary = self.frame.get("Bottom", ())[0]

            if not top_boundary or not bottom_boundary:
                return

            distance_to_top = self.distance_between(self.current_location, top_boundary)
            distance_to_bottom = self.distance_between(self.current_location, bottom_boundary)

            # Check if the current location is closer to the top or bottom boundary
            if distance_to_top < distance_to_bottom:
                # If closer to the top boundary, adjust the trajectory
                self.update_trajectory(self.current_location, self.closest_point_on_trajectory(trajectory=self.bottom_boundary))
            else:
                # If closer to the bottom boundary, adjust the trajectory
                self.update_trajectory(self.current_location, self.closest_point_on_trajectory(trajectory= self.top_boundary))

    def is_inside_frame(self):
        sides = (self.left_boundary, self.bottom_boundary,self.right_boundary,self.top_boundary)
        for side in sides:
            point_on_side = str(self.point_position_relative_to_line(line=side)).lower()
            if(point_on_side == "left" ):
                pass
            else:
                return False
        return True

    def closest_point_on_trajectory(self, trajectory=None):
        point = self.current_location

        if(trajectory==None):
            trajectory = self.trajectory
            start = self.start
            destination = self.destination
        else:
            trajectory = trajectory
            start = trajectory.locations[0]
            destination = trajectory.locations[1]
        """
        Find the closest point on the trajectory to a given point.

        Args:
            point (tuple): GPS coordinates (latitude, longitude) of the point.

        Returns:
            tuple: GPS coordinates of the closest point on the trajectory.
        """
        if not trajectory:
            return None

        # Calculate the closest point on the trajectory using perpendicular distance
        x0, y0 = point
        x1, y1 = start
        x2, y2 = destination

        dx = x2 - x1
        dy = y2 - y1

        if dx == 0 and dy == 0:
            # If start and destination are the same, return start
            return start

        t = ((x0 - x1) * dx + (y0 - y1) * dy) / (dx**2 + dy**2)

        if t < 0:
            # Closest point is before the start of the trajectory
            return start
        elif t > 1:
            # Closest point is after the end of the trajectory
            return destination
        else:
            # Closest point is on the trajectory
            x = x1 + t * dx
            y = y1 + t * dy
            return x, y

    def assign_points_on_boundaries(self, interval_meters):
        """
        Assign points on every n meters of each boundary and name them following the pattern [boundary side]_[i].

        Args:
            interval_meters (float): The interval in meters between each assigned point.
        """
        if not self.frame or len(self.frame) == 0:
            return

        for side, boundary_points in self.frame.items():
            if len(boundary_points) != 2:
                continue

            start_point, end_point = boundary_points
            total_distance = self.distance_between(start_point, end_point)
            # Calculate the number of points to be assigned
            num_points = int(total_distance / interval_meters)
            for i in range(1, num_points + 1):
                # Calculate the position of the point along the boundary
                ratio = i / (num_points + 1)  # Ratio between 0 and 1
                new_point = (
                    start_point[0] + ratio * (end_point[0] - start_point[0]),
                    start_point[1] + ratio * (end_point[1] - start_point[1])
                )
                label = f"point_{side}_{i}"
                marker = folium.Marker(location=new_point, popup=label,color="purple")
                marker.add_to(self.mymap)
                # Assign the new point with the specified name pattern
                point_name = f"{side}_{i}"
                setattr(self, point_name, new_point)