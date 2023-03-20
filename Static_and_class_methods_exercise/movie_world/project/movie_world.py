from .customer import Customer
from .dvd import DVD


class MovieWorld:
    DVD_CAPACITY = 15
    CUSTOMER_CAPACITY = 10

    def __init__(self, name):
        self.name = name
        self.customers = []
        self.dvds = []

    @staticmethod
    def dvd_capacity():
        return MovieWorld.DVD_CAPACITY

    @staticmethod
    def customer_capacity():
        return MovieWorld.CUSTOMER_CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < self.CUSTOMER_CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.DVD_CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id, dvd_id):
        customer = [x for x in self.customers if x.id == customer_id]
        dvd = [x for x in self.dvds if x.id == dvd_id]
        if customer and dvd:
            if dvd[0] in customer[0].rented_dvds:
                return f"{customer[0].name} has already rented {dvd[0].name}"
            if dvd[0] not in customer[0].rented_dvds and dvd[0].is_rented:
                return "DVD is already rented"
            if customer[0].age < dvd[0].age_restriction:
                return f"{customer[0].name} should be at least {dvd[0].age_restriction} to rent this movie"
            dvd[0].is_rented = True
            customer[0].rented_dvds.append(dvd[0])
            return f"{customer[0].name} has successfully rented {dvd[0].name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = [x for x in self.customers if x.id == customer_id]
        dvd = [x for x in self.dvds if x.id == dvd_id]
        if dvd[0] in customer[0].rented_dvds:
            dvd[0].is_rented = False
            customer[0].rented_dvds.remove(dvd[0])
            return f"{customer[0].name} has successfully returned {dvd[0].name}"
        return f"{customer[0].name} does not have that DVD"

    def __repr__(self):
        result = ""
        for number, client in enumerate(self.customers):
            result += f"{client}\n"
        for number, dvd in enumerate(self.dvds):
            result += f"{dvd}\n"
        return result.strip()
