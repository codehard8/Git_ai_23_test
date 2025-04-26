print("This is Bug Hunter Practically!")
print("Testing will help me find bugs that users might encounter")

class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    def power(self, a, b):
        if b < 0:
            return 1 / (a ** abs(b))
        return a ** b

    def factorial(self, n):
        if n < 0:
            raise ValueError("Negative factorial is not defined")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

    def fibonacci(self, n):
        if n < 0:
            raise ValueError("Negative fibonacci is not defined")
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return a
