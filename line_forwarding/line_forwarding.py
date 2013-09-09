import robo3pi as s
import time
import math


def line_follower(id):
    #place on line
    s.readCalibratedSensors(id, 1)
    time.sleep(0.35)
    s.readCalibratedSensors(id, 0)
    time.sleep(0.35)
    start = time.time()
    while time.time() - start < 60:
        # s.readCalibratedSensors(id, 0)
        # time.sleep(0.35)
        pos = s.readLinePosition(id)
        time.sleep(0.2)
        print pos
        if pos != "":
            # get real value of each character
            val = ord(pos[0]) + (ord(pos[1]) << 8) - 2000
            print val
            if val > 1500: # the robot is too right to the line
                s.move(id, 12, -12)
                time.sleep(0.35)
                s.move(id, 12, 12)
                time.sleep(0.35)
            elif val < 500:
                s.move(id, -12, 12)
                time.sleep(0.35)
                s.move(id, 12, 12)
                time.sleep(0.35)
            else:      # the robot is centered on the line
                s.move(id, 12, 12)
                time.sleep(0.35)


def main():
    s.init('/dev/ttyUSB0')
    # s._battary('2')
    # time.sleep(0.5)
    line_follower('2')
    time.sleep(0.2)
    s.stop('2')
    s.close()

main()