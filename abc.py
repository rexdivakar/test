# Simple 40-line Python Script Demo
# Shows loops, functions, classes, & file I/O

import os
import datetime


class Greeter:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}! Welcome to the Python demo."


def square_numbers(n):
    """Return list of squares from 1..n."""
    return [i * i for i in range(1, n + 1)]


def write_to_file(filename, data):
    with open(filename, "w") as f:
        for line in data:
            f.write(str(line) + "\n")


def read_file(filename):
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    user = Greeter("Divakar")
    print(user.greet())

    print("\nGenerating squares up to 10...")
    squares = square_numbers(10)
    print(squares)

    file_name = "output.txt"
    write_to_file(file_name, squares)

    print(f"\nSaved to {file_name} in {os.getcwd()}")
    print("Reading back data...\n")

    content = read_file(file_name)
    print(content)

    print("\nScript finished at:", datetime.datetime.now())
