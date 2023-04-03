from .computer_types.laptop import Laptop
from .computer_types.desktop_computer import DesktopComputer


class ComputerStoreApp:
    def __init__(self):
        self.warehouse = []
        self.profits = []

    def build_computer(self, type_computer, manufacturer, model, processor, ram):
        if type_computer not in ['Desktop Computer', 'Laptop']:
            raise ValueError(f"{type_computer} is not a valid type computer!")
        if type_computer == 'Desktop Computer':
            result = DesktopComputer(manufacturer, model)
            message = result.configure_computer(processor, ram)
            self.warehouse.append(result)
            return message
        result = Laptop(manufacturer, model)
        message = result.configure_computer(processor, ram)
        self.warehouse.append(result)
        return message

    def sell_computer(self, client_budget, wanted_processor, wanted_ram):
        for pc in self.warehouse:
            if pc.price <= client_budget and pc.processor == wanted_processor and pc.ram >= wanted_ram:
                profit = client_budget - pc.price
                self.profits.append(profit)
                return f"{repr(pc)} sold for {client_budget}$."

            raise Exception("Sorry, we don't have a computer for you.")

