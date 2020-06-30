import math
import random
class Dog:
    species = 'mammal'
    def __init__(self,name,age):
        self.name=name
        self.age=age
    # instance method
    def description(self):
        return "{} is {} years old".format(self.name, self.age)

    # instance method
    def speak(self, sound):
        return "{} says {}".format(self.name, sound)

umka = Dog('Umka', 10)
sharik = Dog('Sharik', 7)
print(umka.description())
print(umka.speak("Gruff Gruff"))
