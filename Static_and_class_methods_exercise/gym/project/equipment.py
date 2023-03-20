class Equipment:
    CURRENT_ID = 1

    def __init__(self, name):
        self.name = name
        self.id = self.create_next()

    def create_next(self):
        Equipment.CURRENT_ID += 1
        return Equipment.CURRENT_ID - 1

    @staticmethod
    def get_next_id():
        return Equipment.CURRENT_ID

    def __repr__(self):
        return f"Equipment <{self.id}> {self.name}"

