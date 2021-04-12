"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.base import Vehicle
from homework_02 import exceptions


class Plane(Vehicle):
    cargo = 0.0

    def __init__(self, weight=None, fuel=None, fuel_consumption=None, max_cargo=None):
        self.weight = weight or 1.0
        self.fuel = fuel or 0.0
        self.fuel_consumption = fuel_consumption or 1.0
        self.max_cargo = max_cargo or 0.0
        super().__init__(self.weight, self.fuel, self.fuel_consumption)

    def load_cargo(self, cargo):
        if self.cargo + cargo <= self.max_cargo:
            self.cargo += cargo
        else:
            raise exceptions.CargoOverload

    def remove_all_cargo(self):
        current_cargo = self.cargo
        self.cargo = 0.0
        return current_cargo
