def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

try:
    num = int(input("Enter the position (N) of the Fibonacci number: "))
    if num < 0:
        print("Fibonacci is not defined for negative positions.")
    else:
        print(f"The {num}th Fibonacci number is: {fibonacci(num)}")
except:
    print("Invalid input! Please enter a valid integer.")