import random

# Read names from a file

with open("names.txt") as infile:
    names = [ line.strip() for line in infile ]

# Ask user to enter a number, then randomly choose that many names
# from the list, avoiding any duplicate choices

num = int(input("Enter the amount of names to generate: "))
x = range(0, num)

for n in x:
    print(names[random.randint(1, 1000)])
# Display the chosen names, one per line
