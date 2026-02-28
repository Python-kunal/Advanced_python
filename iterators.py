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


