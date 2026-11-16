import random

# Get user to input how many random numbers they want
num = int(input("Enter the amount of numbers to generate: "))
# Generate this many random numbers
x = range(0, num)
for n in x:
    print(random.randint(1, 100))
# Write the random numbers to a file named random.txt, one number per line