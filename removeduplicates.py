def remove_duplicates(numbers):
    seen = set()
    result = []
    for num in numbers:
        if num not in seen:
            result.append(num)
            seen.add(num)
    return result

nums = [1, 2, 2, 3, 4, 4, 5, 6, 6]
print(remove_duplicates(nums))
