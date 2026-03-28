def add(a, b):
    return a + b

print(add(3, 5))

def greet(name="Guest"):
    return f"Hello, {name}!"

print(greet())
print(greet("Ali"))

def introduce(name, age):
    return f"My name is {name}, and I'm {age} years old."

print(introduce(age=25, name="Ali"))

def square(number):
    return number ** 2

result = square(4)
print(result)

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))