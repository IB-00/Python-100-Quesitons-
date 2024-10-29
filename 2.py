 #2. Write a program that can compute the factorial of a given number. The results should be printed in a
# comma-separated sequence on a single line.
# Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

number = int(input("Enter the Number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(f"The factorial of the entered number {number} is: {factorial}")
