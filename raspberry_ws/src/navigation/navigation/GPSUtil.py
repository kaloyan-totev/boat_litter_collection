import folium
from geopy.distance import geodesic

class GPSUtil:
    def __init__(self, current_location, start=None, destination=None, frame=None):
        self.start = start
        self.destination = destination
        self.current_location = current_location
        self.trajectory = folium.PolyLine(locations=[start, destination], color='blue', popup="Trajectory")
        self.frame = frame

    def distance_between(self, point1, point2):
        # Calculate the difference between two points (gps coordinates)
        return geodesic(point1, point2).meters

    def distance_to_trajectory(self, point):
        # Calculate the distance between a point and the trajectory
        if self.trajectory:
            return self.distance_point_to_line(point, self.start, self.destination)
        else:
            return None

    def update_trajectory(self, start, destination):
        # Update the trajectory between two points
        self.start = start
        self.destination = destination
        self.trajectory = folium.PolyLine(locations=[start, destination], color='blue', popup="Trajectory")

    def update_current_location(self, point):
        # Update the current location
        self.current_location = point

    def update_frame(self, top_left, top_right, bottom_right, bottom_left):
        # Update the frame points
        self.frame = {
            "Top": (top_left, top_right),
            "Right": (top_right, bottom_right),
            "Bottom": (bottom_right, bottom_left),
            "Left": (bottom_left, top_left)
        }

    def visualize_trajectory(self):
        # Create a map centered at the start coordinate
        map_center = self.start
        mymap = folium.Map(location=map_center, zoom_start=15)

        # Add markers for start, destination, and current location
        points = {
            "Starting Point": self.start,
            "Destination Point": self.destination,
            "Current Location": self.current_location,
        }

        for label, point in points.items():
            if point:
                marker = folium.Marker(location=point, popup=label)
                marker.add_to(mymap)

        # Add PolyLine for the trajectory (in blue)
        if self.trajectory:
            self.trajectory.add_to(mymap)

        # Save the map as an HTML file
        mymap.save("trajectory_map.html")

    def plot_map(self):
        # Create a map centered at the start coordinate
        map_center = self.start
        mymap = folium.Map(location=map_center, zoom_start=15)

        # Add markers for start, destination, and current location
        points = {
            "Starting Point": self.start,
            "Destination Point": self.destination,
            "Current Location": self.current_location,
        }

        for label, point in points.items():
            if point:
                marker = folium.Marker(location=point, popup=label)
                marker.add_to(mymap)

        # Add PolyLine for the trajectory (in blue)
        if self.trajectory:
            self.trajectory.add_to(mymap)

            # Plot connections between frame points with labels in green
            if self.frame and len(self.frame) == 4:
                for connection_name, connection_points in self.frame.items():
                    connection = folium.PolyLine(locations=connection_points, color='green', popup=connection_name)
                    connection.add_to(mymap)

        # Save the map as an HTML file
        mymap.save("trajectory_map_with_frame.html")


# Example usage:
start_point = (42.897996, 27.843581)
destination_point = (42.829100, 27.841991)
current_location_point = (42.882054, 27.871513)

# Set frame points
top_left_point = (42.851781, 27.800468)
top_right_point = (42.850520, 27.879634)
bottom_right_point = (42.789835, 27.884055)
bottom_left_point = (42.801670, 27.790202)

trajectory_utility = GPSUtil(start_point, destination_point)
trajectory_utility.update_current_location(current_location_point)
trajectory_utility.update_frame(top_left_point, top_right_point, bottom_right_point, bottom_left_point)

# Plot the map with all points, trajectory, and frame connections
trajectory_utility.plot_map()
