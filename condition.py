user = int(input("Enter your age: "))

if user > 18:
    print("Welcome to the club")

elif user < 18:
    print("Sorry. you are two young")

else:
    print("htt! jaa kr mra le apni bsdk")


#next question:--

user1 = int(input("Enter any number: "))

if user1 % 2 == 0:
    print(f"{user1} is an even number")

else:
    print(f"{user1} is an odd number")


#next question:--

user3 = int(input("Enter your marks: "))

if user3 >= 90 and user3 <= 100:
    print(f"Congratulations! You got an A grade with {user3} marks")
elif user3 >= 80 and user3 <= 89 :
    print(f"Congrats! you got a B grade with {user3} marks")
elif user3 >= 70 and user3 <= 79:
    print(f"Good job! you got a C grade with {user3} marks")
elif user3 <= 70:
    print(f"Fail! you got a D grade with {user3} marks")


#next question:--

user4 = {
    "username": "Kunal gupta",
    "password": "123456"
}

username = input("Enter your username: ")
password = input("Enter your password: ")

if username == user4["username"] and password == user4["password"] :
    print("Login successful! Welcome to the system.")
else:
    print("Invalid username or password. Please try again.")


#next question:--

user5 = int(input("Enter a number to check leap year: "))

if user5 % 4 == 0 and user5 % 100 != 0 or user5 % 400 == 0:
    print(f"{user5} is a leap year")

else:
    print(f"{user5} is not a leap year")

