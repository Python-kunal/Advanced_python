items = ["Milk", "Bread", "Eggs", "Cheese"]

with open("grocery.txt", "w") as file:
    for item in items:
        file.write(item + "\n")

with open("grocery.txt", "r") as file:
    content = file.read()
    print(content)


#next question:--

name = ["Kunal", "Amit", "Rohit", "Sonia"]

with open("names.txt", "w") as file:
    for n in name:
        file.write(n + "\n")


names = input("Enter a name to search: ")

with open("names.txt", "r") as file:
    content = file.read()
    if names in content:
        print(f"{names} is in the file.")
    else:
        print(f"{names} is not in the file.")


#next question:--

with open("server_logs.txt", "w") as file:
    file.write("INFO: System started\n")
    file.write("ERROR: Database connection failed\n")
    file.write("INFO: User logged in\n")
    file.write("ERROR: File not found\n")
    file.write("WARNING: Low memory\n")

with open("server_logs.txt", "r") as file:
    content = file.read()
    print(content)


with open("error_only.txt", "w") as error_file:
    with open("server_logs.txt", "r") as log_file:
        for line in log_file:
            if "ERROR" in line:
                error_file.write(line)
            else:
                print(line)


#next question:--

with open("messages.txt", "w") as file:
    file.write("i hate waiting, i hate traffic")

with open("messages.txt", "r") as file:
    content = file.read()
    print(content)
    with open("positive_messages.txt", "w") as positive_file:
        positive_file.write(content.replace("hate", "love"))
    with open("positive_messages.txt", "r") as positive_file:
        content = positive_file.read()
        print(content)



