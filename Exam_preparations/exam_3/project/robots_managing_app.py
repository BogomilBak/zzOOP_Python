from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService
# from Exam_preparations.exam_3.project.robots.female_robot import FemaleRobot
# from Exam_preparations.exam_3.project.services.main_service import MainService
# from Exam_preparations.exam_3.project.services.secondary_service import SecondaryService
# from Exam_preparations.exam_3.project.robots.male_robot import MaleRobot


class RobotsManagingApp:
    INVALID_ROBOT_TYPE_ERROR_MESSAGE = "Invalid robot type!"
    INVALID_SERVICE_TYPE_ERROR_MESSAGE = "Invalid service type!"
    UNSUITABLE_SERVICE_FOR_ROBOT_ERROR_MESSAGE = "Unsuitable service."
    MAXIMUM_CAPACITY_FOR_SERVICE_ERROR_MESSAGE = "Not enough capacity for this robot!"
    NO_ROBOT_FOUND_IN_THE_GIVEN_SERVICE_ERROR_MESSAGE = "No such robot in this service!"
    SERVICES_UNIQUE_NAMES = {}
    ROBOTS_UNIQUE_NAMES = {}

    def __init__(self):
        self.robots = []
        self.services = []

    def __create_service_by_type(self, service_type, name):
        valid_types = {
            "MainService": MainService,
            "SecondaryService": SecondaryService
        }
        if service_type not in valid_types:
            raise Exception(self.INVALID_SERVICE_TYPE_ERROR_MESSAGE)
        created_service = valid_types[service_type](name)
        return created_service

    def __create_robot_by_type_kind_and_price(self, robot_type, name, kind, price):
        valid_types = {
            "MaleRobot": MaleRobot,
            "FemaleRobot": FemaleRobot
        }
        if robot_type not in valid_types:
            raise Exception(self.INVALID_ROBOT_TYPE_ERROR_MESSAGE)
        robot = valid_types[robot_type](name, kind, price)
        return robot

    def add_service(self, service_type, name):
        if name in self.SERVICES_UNIQUE_NAMES:
            return
        service = self.__create_service_by_type(service_type, name)
        self.SERVICES_UNIQUE_NAMES[name] = service
        self.services.append(service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type, name, kind, price):
        if name in self.ROBOTS_UNIQUE_NAMES:
            return
        robot = self.__create_robot_by_type_kind_and_price(robot_type, name, kind, price)
        self.ROBOTS_UNIQUE_NAMES[name] = robot
        self.robots.append(robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name, service_name):
        robot = self.ROBOTS_UNIQUE_NAMES[robot_name]
        service = self.SERVICES_UNIQUE_NAMES[service_name]
        self.__validate_correct_robot_for_correct_service(robot, service)
        self.__validate_capacity_for_service_by_given_robot(service)
        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name, service_name):
        service = self.SERVICES_UNIQUE_NAMES[service_name]
        robot = self.__validate_robot_in_service_exists(robot_name, service)
        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name):
        service = self.SERVICES_UNIQUE_NAMES[service_name]
        amount = self.__get_amount_of_robots_fed_with_eating_method(service)
        return f"Robots fed: {amount}."

    def service_price(self, service_name):
        service = self.SERVICES_UNIQUE_NAMES[service_name]
        amount = self.__calculate_total_amount_of_robots_by_service(service)
        return f"The value of service {service_name} is {amount:.2f}."

    def __str__(self):
        return '\n'.join([x.details() for x in self.services]).strip()

    def __validate_correct_robot_for_correct_service(self, robot: [MaleRobot, FemaleRobot], service: [MainService, SecondaryService]):
        if not robot.suitable_services == service.get_service_name_by_type:
            return self.UNSUITABLE_SERVICE_FOR_ROBOT_ERROR_MESSAGE
        return True

    def __validate_capacity_for_service_by_given_robot(self, service):
        if len(service.robots) >= service.capacity:
            raise Exception(self.MAXIMUM_CAPACITY_FOR_SERVICE_ERROR_MESSAGE)
        return True

    def __validate_robot_in_service_exists(self, robot_name, service):
        robot = [x for x in service.robots if x.name == robot_name]
        if not robot:
            raise Exception(self.NO_ROBOT_FOUND_IN_THE_GIVEN_SERVICE_ERROR_MESSAGE)
        return robot[0]

    @staticmethod
    def __get_amount_of_robots_fed_with_eating_method(service):
        amount = len([x.eating() for x in service.robots])
        return amount

    @staticmethod
    def __calculate_total_amount_of_robots_by_service(service):
        amount = sum([x.price for x in service.robots])
        return amount







