def get_even_numbers(numbers):
    return [num for num in numbers if num % 2 == 0]

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(get_even_numbers(nums))
