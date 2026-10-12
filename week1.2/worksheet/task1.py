# Worksheet 1.2: Task 1 Solution
import sys

score = input("Enter an integer grade between 0 and 100: ")

if score.isdecimal() and 0 <= int(score) <= 100:
    score = int(score)
    if score >= 70:
        print(f"{score} is a Distinction")
    elif score >= 40:
        print(f"{score} is a Pass")
    else:
        print(f"{score} is a Fail")
else:
        sys.exit("Error: Grade must be an integer between 0 and 100")