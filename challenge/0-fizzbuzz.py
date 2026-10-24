#!/usr/bin/python3
"""
FizzBuzz implementation
"""
import sys


def fizzbuzz(n):
    """
    Prints numbers from 1 to n separated by a space, with:
    - FizzBuzz if divisible by 3 and 5
    - Fizz if divisible by 3
    - Buzz if divisible by 5
    """
    if n < 1:
        return

    result = []
    for i in range(1, n + 1):
        # Check for both 3 and 5 first
        if (i % 3 == 0) and (i % 5 == 0):
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    print(" ".join(result))


if __name__ == "__main__":
    if len(sys.argv) > 1:
        fizzbuzz(int(sys.argv[1]))
        


