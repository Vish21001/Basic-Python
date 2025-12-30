numbers = [1, 2, 2, 3, 4, 4, 5]
numbers2 = [4, 5, 6, 6, 7, 8, 8]
unique_numbers = []
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)
for number in numbers2:
    if number not in unique_numbers:
        unique_numbers.append(number)
unique_numbers.sort()
print(unique_numbers)
