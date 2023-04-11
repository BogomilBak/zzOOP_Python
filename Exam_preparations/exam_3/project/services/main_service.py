from project.services.base_service import BaseService
# from Exam_preparations.exam_3.project.services.base_service import BaseService


class MainService(BaseService):
    def __init__(self, name):
        super().__init__(name, capacity=30)

    @property
    def get_service_name_by_type(self):
        return "Main Service"
