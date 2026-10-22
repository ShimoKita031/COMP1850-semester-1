# Week 4, Session 2: Task 2

# Given an incomplete function odd_even and a docstring.
# Your task is to complete the function based on the details
# in the docstring.


def odd_even(lstIntegers):
    """
    This function takes a list of integers and returns the number of
    odd numbers and the number of even numbers in a list.

    Args:
        lstIntegers (list): A list of integers.

    Returns:
        list: A list containing [odd_count, even_count].
    """
    oddcounter = 0
    evencounter = 0

    for item in lstIntegers:
        if item % 2 == 0:
            evencounter += 1
        else:
            oddcounter += 1
    return oddcounter, evencounter
    # Complete your code here


# Check if correct output is produced
print(odd_even([1, 2, 3, 4, 5]))  # Output: [3, 2]
