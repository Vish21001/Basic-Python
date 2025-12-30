numbers = [1, 2, 3, 4, 5]
max_number = numbers[0]

for number in numbers:
    if number > max_number:
        max_number = number
print(f"The maximum number is: {max_number}")
