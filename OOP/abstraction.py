"""
hiding complex details and only showing essential details

"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass #no implemntation

class Car(Vehicle):
    def start(self):
        print("Car Start with Key")

class Bike(Vehicle):
    def start(self):
        print("Bike Start with buton")

car = Car()
bike = Bike()

car.start()
bike.start()