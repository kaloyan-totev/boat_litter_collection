from GPSUtil import GPSUtil

top_left_point = (42.65585256186259, 27.57744174007652)
top_right_point = (42.655882914489375, 27.577553290251092)
bottom_right_point = (42.655788810269485, 27.577632932122935)
bottom_left_point = (42.65574973707147, 27.577530671961426)
current = (42.65583022937629, 27.5775306523617)
frame = (top_left_point,top_right_point,bottom_right_point,bottom_left_point)

util = GPSUtil(current_location = current  ,frame=frame)

util.adjust_trajectory_to_boundary()
util.plot_map()

while(True):
    newdata = self.ser.readline()
    print(f"newdata[0:6] : {newdata[0:6]}")
    if newdata[0:6] == "$GPRMC":
        newmsg = pynmea2.parse(newdata)
        lat = newmsg.latitude
        lng = newmsg.longitude
        gps = "Latitude=" + str(lat) + "and Longitude=" + str(lng)
        self.util.update_current_location((lat, lng))
        print(gps)