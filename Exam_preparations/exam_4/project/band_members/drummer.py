# from Exam_preparations.exam_4.project.band_members.musician import Musician
from project.band_members.musician import Musician


class Drummer(Musician):
    @property
    def skills_available_to_be_learned(self):
        return [
            "play the drums with drumsticks",
            "play the drums with drum brushes",
            "read sheet music"
        ]

    @staticmethod
    def get_class_name_by_type():
        return "Drummer"
