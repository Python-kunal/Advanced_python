colors = ["Red", "Green", "Blue"]

color_iterator = iter(colors)

print(next(color_iterator))
print(next(color_iterator))
print(next(color_iterator))

try :
    print(next(color_iterator))

except StopIteration:
    print("No more colors to iterate over")


#next question:--

string = "Code"
bookmark = iter(string)

for letter in bookmark:
    print(letter)

for letter in bookmark:
    print(letter)

print("---program finished---")


#next question:--

class Countup:
    def __init__(self, limit):
        self.limit = limit
        self.count = 1

    def __iter__(self):
        return self

    def __next__(self):
        self.count += 1
        if self.count > self.limit:
            raise StopIteration
        else:
            return self.count - 1

counter = Countup(10)
for number in counter:
    print(number)


#next question:--

class ReverseText:
    def __init__(self, text):
        self.text = text
        self.index = (len(text))

    def __iter__(self):
        return self

    def __next__ (self):
        if self.index == 0:
            raise StopIteration
        else:
            self.index -= 1
            return self.text[self.index]

reverse_text = ReverseText("Python")
for char in reverse_text:
    print(char)

print("---program finished---")


#next question:--

import random
class InfiniteDice:
    def __init__(self):
        pass
    def __iter__(self):
        return self
    def __next__(self):
        return random.randint(1,6)

dice = InfiniteDice()
for _ in range(10):
    print(next(dice))

