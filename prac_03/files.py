# Task 1: Write user's name to a file called "name.txt"
name = input("Enter your name: ")

with open("name.txt", "w") as file:
    file.write(name)

# Task 2: Read name from "name.txt" and print it
with open("name.txt", "r") as file:
    name = file.read()
    print(f"Your name is {name}")

# Task 3: Read the first two numbers from "numbers.txt" and add them together
with open("numbers.txt", "r") as file:
    line1 = int(file.readline().strip())
    line2 = int(file.readline().strip())
    result = line1 + line2
    print(f"The sum of the first two numbers is: {result}")

# Task 4: Read all numbers from "numbers.txt" and calculate their total
total = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total += int(line.strip())

print(f"The total of all numbers in the file is: {total}")