def factorial(n):
    if n < 0:
        return "Invalid input. Enter a non-negative integer."
    elif n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


num = int(input("Enter a non-negative integer: "))
result = factorial(num)
print(f"Factorial of {num} is: {result}")
