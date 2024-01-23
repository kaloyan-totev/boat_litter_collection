from arduinoCommandCenter import Command
import time

cmd = Command()
inp = None
while(str(inp) != "q"):
    print("started")
    inp = input()

    if(str(inp) == "0"):
        cmd.stop_motors()
        print("stop_motors")
    elif(str(inp) == "1"):
        cmd.go_forward()
        print("go_forward")
    elif(str(inp) == "2"):
        cmd.go_left()
        print("go_left")
    elif(str(inp) == "3"):
        cmd.go_right()
        print("go_right")
    elif(inp == 4):
        cmd.go_forward()
        print("go_forward")
