def calculate_average(numbers):
    sum = 0
    for num in numbers:
    sum += num
    return sum / len(numbers)

nums = [10, 20, 30, 40, 50]
print(f"The average is {calculate_average(nums)}")