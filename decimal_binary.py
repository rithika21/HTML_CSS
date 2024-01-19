def decimal_to_binary(decimal_num):
    binary_num = bin(decimal_num).replace("0b", "")
    return binary_num

# Get user input for a decimal number
decimal_input = int(input("Enter a decimal number: "))

# Convert to binary and print the result
binary_result = decimal_to_binary(decimal_input)
print(f"The binary representation of {decimal_input} is: {binary_result}")

