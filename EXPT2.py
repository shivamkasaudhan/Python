# Input the value of n
n = int(input("Enter the value of n: "))
# Initialize variables
count = 0
num = 2
print("First", n, "prime numbers are:")
while count < n:
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num, end=" ")
        count += 1
    num += 1
