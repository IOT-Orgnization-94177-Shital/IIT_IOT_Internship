
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
import calculator
print("Add:", calculator.add(10, 5))
print("Subtract:", calculator.subtract(10, 5))
print("Multiply:", calculator.multiply(10, 5))
print("Divide:", calculator.divide(10, 5))
