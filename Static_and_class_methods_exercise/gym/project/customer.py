class Customer:
    CURRENT_ID = 1

    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
        self.id = self.create_next()

    def create_next(self):
        Customer.CURRENT_ID += 1
        return Customer.CURRENT_ID - 1

    @staticmethod
    def get_next_id():
        return Customer.CURRENT_ID

    def __repr__(self):
        return f"Customer <{self.id}> {self.name}; Address: {self.address}; Email: {self.email}"
