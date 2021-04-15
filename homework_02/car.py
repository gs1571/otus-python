"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Car(Vehicle):

    def __init__(self, weight=None, fuel=None, fuel_consumption=None):
        self.engine = None
        super().__init__(weight, fuel, fuel_consumption)

    def set_engine(self, engine):
        self.engine = engine
