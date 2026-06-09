'''
This Python program accepts two numbers from the user and calculates the difference between them. 
It compares the two numbers and subtracts the smaller number from the larger number, ensuring that the result is always positive or zero. 
The program then displays the subtraction operation and its result.
'''

# Input two numbers
A = float(input("Enter the value of A: "))
B = float(input("Enter the value of B: "))

# Check if A is greater than B
if A >= B:
    difference = A - B
    print(f"{A} - {B}  =  {difference}")

# Check if B is greater than A
else:
    difference = B - A
    print(f" {B} - {A} =  {difference}")

