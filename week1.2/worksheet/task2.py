# Worksheet 1.2: Task 2 Solution
from util import read_numbers
import sys

try:
    numbers = read_numbers()

    #Find minimum, maximum and mean
    minimum = min(numbers)
    maximum = max(numbers)
    mean = sum(numbers) / len(numbers)

    #Find median
    numbers.sort()
    if len(numbers) % 2 == 1:
        median = numbers[len(numbers) // 2]
    else:
        n = len(numbers)
        median = (numbers[n // 2 - 1] + numbers[n // 2]) / 2

    print(f"Minimum = {minimum}")
    print(f"Maximum = {maximum}")
    print(f"Mean = {mean}")
    print(f"Median: {median}")

except:
    sys.exit("Error: no numbers provided")