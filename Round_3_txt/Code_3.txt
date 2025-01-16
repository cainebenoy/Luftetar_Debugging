def find_max(lst):
    max = lst[0]
    for num in lst:
    if num > max:
        max = num
    return max

numbers = [3, 1, 4, 1, 5, 9]
print("The maximum number is:", find_maximum(numbers))
