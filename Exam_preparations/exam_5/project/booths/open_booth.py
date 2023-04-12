# from Exam_preparations.exam_5.project.booths.booth import Booth
from project.booths.booth import Booth


class OpenBooth(Booth):
    @property
    def get_class_name(self):
        return "Open Booth"

    @property
    def price_per_boot_type(self):
        return 2.5
