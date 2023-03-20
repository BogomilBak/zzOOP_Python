class Subscription:
    DEFAULT_ID = 1

    def __init__(self, date, customer_id, trainer_id, exercise_id):
        self.date = date
        self.customer_id = customer_id
        self.trainer_id = trainer_id
        self.exercise_id = exercise_id
        self.id = self.create_next()

    def create_next(self):
        Subscription.DEFAULT_ID += 1
        return Subscription.DEFAULT_ID - 1

    @staticmethod
    def get_next_id():
        return Subscription.DEFAULT_ID

    def __repr__(self):
        return f"Subscription <{self.id}> on {self.date}"

