#!/usr/bin/python3
def fizzbuzz():
    for i in range(0, 101):
        if i == 100:
            print("Buzz")
            break
        if i % 5 == 0 and i % 3 == 0:
            print("FizzBuzz ", end="")
        elif i % 5 == 0 and i % 3 != 0:
            print("Buzz ", end="")
        elif i % 5 != 0 and i % 3 == 0:
            print("Fizz ", end="")
        else:
            print(f"{i}", end="")
