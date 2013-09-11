__author__ = 'artyom'


class Robot():
    def __init__(self, robotId, speed, pos_x, pos_y, angle):
        self.id = robotId
        self.speed_ = speed
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.angle = angle
        self.change_pos_x = pos_x
        self.change_pos_y = pos_y
        self.change_speed = speed
        self.change_angle = angle
        self.linear_speed_x = 0.0
        self.linear_speed_y = 0.0
        self.start_pos_x = pos_x
        self.start_pos_y = pos_y
        self.start_angle = angle
        self.right_wheel_speed = 0
        self.left_wheel_speed = 0

    def setPosition(self, x, y):
        self.pos_x = x
        self.pos_y = y

    def setChangePosition(self, x, y):
        self.change_pos_x = x
        self.change_pos_y = y

    def setAngle(self, angle):
        self.angle = angle

    def setChangeAngle(self, angle):
        self.change_angle = angle

    def setSpeed(self, speed):
        self.speed = speed

    def setChangeSpeed(self, change_speed):
        self.change_speed = change_speed

    def setLinearSpeed(self, speed_x, speed_y):
        self.linear_speed_x = speed_x
        self.linear_speed_y = speed_y

    def setStartPos(self, x, y):
        self.start_pos_x = x
        self.start_pos_y = y

    def setStartAngle(self, angle):
        self.start_angle = angle

    def getId(self):
        return self.id

    def getRobotPos(self):
        return self.pos_x, self.pos_y

    def getPosX(self):
        return self.pos_x

    def getPosY(self):
        return self.pos_y

    def setSpeedOnWheels(self, left_wheel, right_wheel):
        self.left_wheel_speed = left_wheel
        self.right_wheel_speed = right_wheel