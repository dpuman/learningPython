#This is bad
class Employee:
    def greet(self):
        print("Employee")


class Person:
    def greet(self):
        print("Persoin")


class Manager(Employee, Person):
    pass


man = Manager()
man.greet()

# Right


class Flyeer:
    def Flying(self):
        print("Flying")


class Swimmer:
    def swimmer(self):
        print("Swim")


class FlyingSwimmer(Flyeer, Swimmer):
    pass


fl = FlyingSwimmer()
fl.Flying()
