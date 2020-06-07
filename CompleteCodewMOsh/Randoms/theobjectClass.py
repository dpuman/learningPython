class Animal:
    def __init__(self):
        self.age = 1

    def eat(self):
        print("Eating")

#Animal is parent or base
#Mammal is child or sub


class Mammal(Animal):
    def walk(self):
        print("Walking")


class Fish(Animal):
    def swim(self):
        print("Swimming")


mam = Mammal()
mam.eat()
print(mam.age)

print(isinstance(mam, object))
print(isinstance(mam, Animal))
o = object()
# o.

print(issubclass(Fish, Animal))
