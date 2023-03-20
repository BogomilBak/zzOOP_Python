class Trainer:
    DEFAULT_ID = 1

    def __init__(self, name):
        self.name = name
        self.id = self.create_next()

    def create_next(self):
        Trainer.DEFAULT_ID += 1
        return Trainer.DEFAULT_ID - 1

    @staticmethod
    def get_next_id():
        return Trainer.DEFAULT_ID

    def __repr__(self):
        return f"Trainer <{self.id}> {self.name}"
