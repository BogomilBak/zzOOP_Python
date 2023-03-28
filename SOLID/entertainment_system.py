import abc


class EntertainmentDevice(abc.ABC):
    def __init__(self, power=False):
        self.power = power

    def connect_to_device(self, device):
        if not self.power:
            return "You need to turn the power on first!"
        if device.__class__ not in self.devices_possible():
            return f"{self.__class__.__name__} cannot connect to {device.__class__.__name__}!"
        return f"{self.__class__.__name__} is connected to {device.__class__.__name__} via {self.cable_needed(device)} cable"

    def connect_to_power_outlet(self):
        if self.power:
            return f"{self.__class__.__name__} power is already on!"
        self.power = True
        return f"{self.__class__.__name__} power is on"

    def cable_needed(self, device):
        if device.__class__ in self.devices_possible():
            return self.devices_possible()[device.__class__]

    @abc.abstractmethod
    def devices_possible(self):
        pass


class Television(EntertainmentDevice):

    def devices_possible(self):
        return {
            GameConsole: "HDMI",
            Router: "ethernet"
        }


class DVDPlayer(EntertainmentDevice):

    def devices_possible(self):
        return {
            Television: "HDMI",
        }


class GameConsole(EntertainmentDevice):

    def devices_possible(self):
        return {
            Television: "HDMI",
            Router: "ethernet"
        }


class Router(EntertainmentDevice):

    def devices_possible(self):
        return {
            Television: "ethernet",
            GameConsole: "ethernet",
        }


tv = Television()
router = Router()
print(tv.connect_to_power_outlet())
print(tv.connect_to_device(router))
