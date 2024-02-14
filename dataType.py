numeric_string = "abc"
try:
    integer_value = int(numeric_string)
    print(integer_value)
except ValueError:
    print("Invalid")

age = input("Enter your age: ")
print("hello! you are ",age," years old.")