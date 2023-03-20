from .customer import Customer
from .equipment import Equipment
from .exercise_plan import ExercisePlan
from .subscription import Subscription
from .trainer import Trainer


class Gym:
    def __init__(self):
        self.customers = []
        self.trainers = []
        self.equipment = []
        self.plans = []
        self.subscriptions = []

    def add_customer(self, customer: Customer):
        if customer in self.customers:
            return
        self.customers.append(customer)

    def add_trainer(self, trainer: Trainer):
        if trainer in self.trainers:
            return
        self.trainers.append(trainer)

    def add_equipment(self, equipment: Equipment):
        if equipment in self.equipment:
            return
        self.equipment.append(equipment)

    def add_plan(self, plan: ExercisePlan):
        if plan in self.plans:
            return
        self.plans.append(plan)

    def add_subscription(self, subscription: Subscription):
        if subscription in self.subscriptions:
            return
        self.subscriptions.append(subscription)

    def __get_by_id(self, entities, entity_id):
        for entity in entities:
            if entity.id == entity_id:
                return entity

    def subscription_info(self, subscription_id):
        subscription = self.__get_by_id(self.subscriptions, subscription_id)
        customer = self.__get_by_id(self.customers, subscription.customer_id)
        trainer = self.__get_by_id(self.trainers, subscription.trainer_id)
        exercise_plan_id = subscription.exercise_id
        plan = self.__get_by_id(self.plans, exercise_plan_id)
        equipment_id = plan.equipment_id
        equipment = self.__get_by_id(self.equipment, equipment_id)
        return repr(subscription) + '\n' + repr(customer) + '\n' + repr(trainer) + '\n' + repr(equipment) + '\n' + repr(plan)



