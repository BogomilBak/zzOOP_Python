# from Exam_preparations.exam_7.project.horse_specification.horse import Horse
from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    @property
    def speed_increased_from_training(self):
        return 2

    @property
    def breed_maximum_speed(self):
        return 120
