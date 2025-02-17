class PublicClass:
    def __init__(self):
        self.name = "Rohith"

    def display_name(self):
        print(self.name)

obj = PublicClass()
obj.display_name()  # This will print "Rohith"

## protected method

class Protected:
    def __init__(self):
        self._age = 30  # Protected attribute

class Subclass(Protected):
    def display_age(self):
        print(self._age)  # Accessible in subclass

obj = Subclass()
obj.display_age()

