## The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators
## *** With the same name that can be executed on many objects or classes.
## Class Polymorphism
## Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.

class Car:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def moveMax(self):
        return "120 k/h"

    def __str__(self):
        return f"brand : {self.brand} , model : {self.model}"


## Inheritance Class Polymorphism
## i don't need brand, model because i inherit from Car class
class EuroCar(Car):

    def moveMax(self):
        return "160 k/h"


class ChinaCar(Car):

    def __init__(self, brand, model, maxSpeed):
        super().__init__(brand, model)
        self.maxSpeed = maxSpeed

    def moveMax(self):
        return f"{self.maxSpeed} k/h"


car = Car("Toyota", "Revo 5 2024")
print(car, ",max speed :", car.moveMax())
euroCar = EuroCar("BMW", "i350 1998")
print(euroCar, ",max speed :", euroCar.moveMax())
chinaCar = ChinaCar("BYD", "SEAL", "190")
print(chinaCar, ",max speed :", chinaCar.moveMax())
