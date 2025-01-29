from abc import ABC, abstractmethod  # can create interfaces with library ABC

"""
Python’s dynamic nature allows you to implement an informal interface.
An informal Python interface is a class that defines methods that can be overridden,
but there’s no strict enforcement.
"""
# Declare Interfaces
class SoundAnimal :
    """
       The pass statement is used as a placeholder for future code.
       When the pass statement is executed, nothing happens,
       but you avoid getting an error when empty code is not allowed.
    """
    def getSound(self,sound:str) -> str: # this method return string type
        """ do something """
        pass


# Way to imprement interface class
class Dog(SoundAnimal) :
    def getSound(self,sound:str) -> str:
        return f"It's sound like {sound}"




# จากนั้นทำการสืบทอดคลาส ABC ให้กับคลาสที่เราต้องการจะให้เป็น interface ในที่นี้เราต้องการให้คลาส MathBasic เป็น interface เราจึงต้องให้ fly_behavior สืบทอดคลาส ABC เข้าไป
class MathBasic(ABC):
    @abstractmethod # mark this method is abstarct
    def getResult(self, x: int , y:int):  # this is void
        """ do something """
        pass


class Robot(MathBasic) :
    def getResult(self, x: int , y:int) :
        print(f"I know {x} x {y} is {x*y}")



# Apply with Generic
# print(Dog().getSound("Hong Hong!"))
# Robot().getResult(-35,7598)

