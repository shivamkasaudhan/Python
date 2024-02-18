# Define the range of numbers (start, stop, step)
start = 1  # Starting number
stop = 11  # Ending number (exclusive)
step = 2   # Step size

# Create an empty list to store the numbers
numbers_list = []

# Loop through the range of numbers
for num in range(start, stop, step):
    # Append each number to the list
    numbers_list.append(num)

# Print the list of numbers
print("List of numbers:", numbers_list)
