from car import Car
import random


class UnreliableCar(Car):
    """Derived class of Car that has a chance of not driving when asked."""

    def __init__(self, name, fuel, reliability):
        """Initialize an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if a random number is less than the car's reliability."""
        if random.randint(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
