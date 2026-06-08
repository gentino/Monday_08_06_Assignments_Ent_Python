# Input two numbers
A = float(input("Enter the value of A: "))
B = float(input("Enter the value of B: "))

# Check if A is greater than B
if A >= B:
    difference = A - B
    print(f"{A} - {B}  =  difference")

# Check if B is greater than A
else:
    difference = B - A
    print(f" {B} - {A} =  difference")

