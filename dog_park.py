class Dog:
    species = 'mammal'
    
    def __init__(self,name, age):
        self.name = name
        self.age = age
    
    def description(self):
        return ("{} is {} years old".format(self.name,self.age))

    def speak(self,sound):
        return ("{} says {}".format(self.name,sound))

class DvorStvor(Dog):
    def run(self,speed):
        return ("{} runs {}".format(self.name,speed))
class NewParoda(Dog):
    def run(self,speed):
        return ("{} runs {}".format(self.name, speed))

umka = DvorStvor('Umka',10)
print(umka.description())
print(umka.run('as shit'))
