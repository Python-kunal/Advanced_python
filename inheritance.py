class Animal:
    def habitat(self):
        print("Animal lives one Earth")

class Dog(Animal):
    pass

habitation = Dog()
habitation.habitat()


#next question:--

class Animal:
    def __init__(self, name):
        self.name = name

    def habitat(self):
        print("Animal lives on earth")

class Dog(Animal):
    def __init__(self):
        super().__init__("dog")

ani = Dog()
ani.habitat()
print(ani.name)