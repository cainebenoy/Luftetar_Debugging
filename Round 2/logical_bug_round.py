def find_gcd(a, b):
    while a != b:
        if a > b:
            b = b - a
        else:
            a = a - b
    return a

try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    if num1 < 0 or num2 < 0:
        print("GCD is not defined for negative numbers.")
    elif num1 == 0 or num2 == 0:
        print("The GCD of", num1, "and", num2, "is:", max(num1, num2))
    else:
        print("The GCD of", num1, "and", num2, "is:", find_gcd(num1, num2))
except:
    print("Invalid input! Please enter valid integers.")