user = int(input("Enter your number: "))

for i in range(1, 11):
    print(f"{user} x {i} = {user * i}")


#next question:--

i = 0
while i < 11:
    print(i)
    i = i + 1


#next question:--


while user != "yes":
    user = input("Are we there yet: ")
    print("Finally!")


#next question:--

for i in range(1,11):
    if i % 2 != 0:
        continue
    print(i)

