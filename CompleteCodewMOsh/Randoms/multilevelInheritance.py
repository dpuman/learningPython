class Animal:
    def walk(self):
        print("Walking")


class Mammal(Animal):
    def eat(self):
        print("Eating")


class Fish(Mammal):
    pass


f = Fish()
#This is bad
f.walk()
