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


#next question:--

class Animal:
    def speak(self):
        print("Animals makes a sound")

class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

bark = Dog()
bark.speak()


#next question:--

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name,age)
        self.student_id = student_id

        print(f"Name: {self.name}, Age: {self.age}, Student ID: {self.student_id}")

        #student = Student("Alice", 21, "S12345")

human = Student("Bob", 22, "S54321")
human.__init__(human.name, human.age, human.student_id)


#next question:--

class Vehicle:
    def start_engine(self):
        print("Engine started")

class Car(Vehicle):
    def drive(self):
        print("car is driving")

class SportsCar(Car):
    def activate_turbo(self):
        print("Turbo mode activated")

my_car = SportsCar()
my_car.activate_turbo()


#next question:--

class Shape:
    def area(self):
        print("Calculating area...")

class Circle(Shape):
    def 
