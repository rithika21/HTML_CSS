def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Get user input for the desired Fibonacci number
try:
    n = int(input("Enter a positive integer to find the Fibonacci number: "))
    result = fibonacci(n)
    print(f"The {n}th Fibonacci number is:", result)
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")

