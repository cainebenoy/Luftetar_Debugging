def reverse_string(s)
    reversed_s = ""
    for char in s
        reversed_s = char + reversed_s
    return reversed_s

string = input("Enter a string: ")
print(f"The reverse of the string is: {reverse_string(string)}")
