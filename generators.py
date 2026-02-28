
def snack_machine():
    yield "snack"
    yield "chocolate"
    yield "chips"

machine = snack_machine()
print(next(machine))
print(next(machine))
print(next(machine))


#next question:--

def generate_evens(limit):
    for num in range(limit):
        if num % 2 == 0:
            print(f"yielding even numbers: {num}")
            yield num

for num in generate_evens(10):
    print(f"received in main code: {num}\n")


#next question:--

