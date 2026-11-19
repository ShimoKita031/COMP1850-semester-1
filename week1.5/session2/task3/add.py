# Week 1.5, Session 2: Task 3

# Write a program here that creates two Money objects, prints them,
# then adds them together and prints their sum

from money import Money
money1 = Money(3, 99)
money2 = Money(4, 57)
print(Money.__add__(money1, money2))