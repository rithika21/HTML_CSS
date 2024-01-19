# Define the list of numbers
numbers = [14, 7, 91, 9, 1, 20, 10]

# Iterate over the list and split each number into its individual digits
individual_digits = []
for number in numbers:
    digits = [int(digit) for digit in str(number)]
    individual_digits.extend(digits)

# Sort the list of individual digits in descending order
sorted_digits_descending = sorted(individual_digits, reverse=True)

# Convert the sorted list of digits to a string
result = ''.join(str(digit) for digit in sorted_digits_descending)

# Print the sorted individual digits in descending order without commas and brackets
print(result)