from project.robots.base_robot import BaseRobot
# from Exam_preparations.exam_3.project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    def __init__(self, name, kind, price):
        super().__init__(name, kind, price, weight=7)

    @property
    def weight_increment(self):
        return 1

    @property
    def suitable_services(self):
        return "Secondary Service"
