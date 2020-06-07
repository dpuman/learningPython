class Animal:
    def __init__(self):
        print("Animal")
        self.age = 1

    def eat(self):
        print("Eating")

#Animal is parent or base
#Mammal is child or sub


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mamal")
        self.weight = 4

    def walk(self):
        print("Walking")


class Fish(Animal):
    def swim(self):
        print("Swimming")


mam = Mammal()
print(mam.weight)
print(mam.age)
