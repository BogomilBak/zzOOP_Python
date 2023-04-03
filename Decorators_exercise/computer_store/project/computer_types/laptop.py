from .computer import Computer


class Laptop(Computer):
    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        processor_prices = {
            "AMD Ryzen 9 5950X": 900,
            "Intel Core i9-11900H": 1050,
            "Apple M1 Pro": 1200
        }
        if processor not in processor_prices:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if ram > 64 or ram % 2 != 0:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")
        self.ram = ram
        self.processor = processor
        price = (ram * 50) + processor_prices[processor]
        self.price = price
        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {price}$."

    def recu(self, n):
        if n == 2:
            return 1
        return self.recu(n - 1)
