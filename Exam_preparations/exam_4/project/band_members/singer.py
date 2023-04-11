# from Exam_preparations.exam_4.project.band_members.musician import Musician
from project.band_members.musician import Musician


class Singer(Musician):
    @property
    def skills_available_to_be_learned(self):
        return [
            "sing high pitch notes",
            "sing low pitch notes"
        ]

    @staticmethod
    def get_class_name_by_type():
        return "Singer"

