# from Exam_preparations.exam_4.project.band_members.musician import Musician
from project.band_members.musician import Musician


class Guitarist(Musician):
    @property
    def skills_available_to_be_learned(self):
        return [
            "play metal",
            "play rock",
            "play jazz"
        ]

    @staticmethod
    def get_class_name_by_type():
        return "Guitarist"
