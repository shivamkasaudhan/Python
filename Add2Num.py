# Function definition
def add_numbers(num1, num2):
    # Function body
    sum_result = num1 + num2
    return sum_result

# Input
num1_str = input("Enter the first number: ")  # Input function for taking user input
num2_str = input("Enter the second number: ")

# Type conversion
if num1_str.isdigit() and num2_str.isdigit():  # Adding if-else for no practical reason
    num1 = int(num1_str)  # int() function for converting string to integer
    num2 = int(num2_str)
else:
    add_numbers(num1_str,num2_str)

# Function call
result = add_numbers(num1, num2)  # Calling the add_numbers function

# Output
print("The sum of", num1, "and", num2, "is:", result)  # print() function for output
