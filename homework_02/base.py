from abc import ABC
from homework_02 import exceptions


class Vehicle(ABC):
    started = False

    def __init__(self, weight=None, fuel=None, fuel_consumption=None):
        self.weight = weight or 1.0
        self.fuel = fuel or 0.0
        self.fuel_consumption = fuel_consumption or 1.0

    def start(self):
        if self.fuel > 0.0:
            self.started = True
        else:
            raise exceptions.LowFuelError

    def move(self, distance):
        if self.fuel > 0 and self.fuel/self.fuel_consumption > distance:
            self.fuel -= distance * self.fuel_consumption
        else:
            raise exceptions.NotEnoughFuel


