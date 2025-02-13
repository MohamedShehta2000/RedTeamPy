#!usr/bin/env python3
def sum():
    x = 3
    y = 4
    return x + y
new = sum()
print(new)

def sum(x):
    y = 4
    return x + y
new = sum(100)
print(new)

def sum(x, y):
    word = f"the sum of {x} and {y} is {x + y}"
    return word
new = sum(100, 200)
print(new)