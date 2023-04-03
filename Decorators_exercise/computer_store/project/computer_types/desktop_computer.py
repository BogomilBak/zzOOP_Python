from .computer import Computer


class DesktopComputer(Computer):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        processor_prices = {
            "AMD Ryzen 7 5700G" : 500,
            "Intel Core i5-12600K": 600,
            "Apple M1 Max": 1800
        }
        if processor not in processor_prices:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")
        if ram > 128 or ram % 2 != 0:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")
        self.ram = ram
        self.processor = processor
        price = (ram * 50) + processor_prices[processor]
        self.price = price
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {price}$."
