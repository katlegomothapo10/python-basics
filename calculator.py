def add(a, b):
    return a + b


def subtract(c, d):
    return c - d


def multiply(e, f):
    return e * f


def divide(g, h):
    if h == 0:
        return "you cannot divide a number with 0"
    return g/h


print("python calculator")
x = int(input("enter your first number: "))
y = int(input("enter your second number: "))

print(add(x, y))
print(subtract(x, y))
print(multiply(x, y))
print(divide(x, y))
