__author__ = 'artyom'


def init_robots(num_of_robots, linear_errors, angle_errors):
    robots = list()
    for i in range(num_of_robots):
        robot = Robot(str(i + 1), linear_errors[i], angle_errors[i])
        robots.append(robot)
    return robots


class Robot():
    def __init__(self, robot_id, linear_error, angle_error):
        self.robot_id = robot_id
        self.linear_error = linear_error
        self.angle_error = angle_error
