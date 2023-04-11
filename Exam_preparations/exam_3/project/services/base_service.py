import abc


class BaseService(abc.ABC):
    BASE_SERVICE_CAPACITY_LESS_THAN_ZERO_ERROR_MESSAGE = "Service capacity cannot be less than or equal to 0!"
    BASE_SERVICE_EMPTY_NAME_ERROR_MESSAGE = "Service name cannot be empty!"

    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.robots = []
        
    @property
    def name(self):
        return self.__name 
    
    @name.setter
    def name(self, value):
        if not value or value.isspace() or not isinstance(value, str):
            raise ValueError(BaseService.BASE_SERVICE_EMPTY_NAME_ERROR_MESSAGE)
        self.__name = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value <= 0 or not isinstance(value, int):
            raise ValueError(BaseService.BASE_SERVICE_CAPACITY_LESS_THAN_ZERO_ERROR_MESSAGE)
        self.__capacity = value

    @property
    @abc.abstractmethod
    def get_service_name_by_type(self):
        pass

    def details(self):
        robots = "Robots: none"
        if self.robots:
            robots = f"Robots: {' '.join([x.name for x in self.robots])}"
        return f'''{self.name} {self.get_service_name_by_type}:
{robots}'''
