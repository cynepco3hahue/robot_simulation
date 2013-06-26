__author__ = 'artyom'


class Robot():
    def __init__(self, robotId, speed, pos_x, pos_y, angle):
        self.id = robotId
        self.speed = speed
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.angle = angle

    def setPosition(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def setAngle(self, angle):
        self.angle = angle

    def setSpeed(self, speed):
        self.speed = speed