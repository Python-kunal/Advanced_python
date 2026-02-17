try:
    word = "PYTHON"
    user = int(input("Enter a number:"))
    print(word[user])

except ValueError:
    print("Please enter a valid number.")
except IndexError:
    print("Error: Index out of range. Please enter a number between 0 and 5")


#next question:--

def add_two_numbers(a,b):
    return a + b
try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    total = add_two_numbers(num1,num2)

    print(f"Sum of {num1} and {num2} is {total}")

except ValueError:
    print("Please enter valid numbers.")



#next question:--

