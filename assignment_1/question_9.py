'''
This Python program generates the Fibonacci sequence up to a number of terms specified by the user. 
The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, 
starting from 0 and 1. The program stores the generated values in a list and then displays the full sequence.
'''

# FIBONACCI SEQUENCE GENERATOR
# Ask the user how many Fibonacci numbers to generate
count = int(input("Enter number of Fibonacci terms to generate: "))

# Initialize the first two Fibonacci numbers
previous_number_2 ,previous_number_1 = 0, 1 

# List to store the Fibonacci sequence
fibonacci_sequence = []

# Generate Fibonacci sequence
for _ in range(count):

    # Append current Fibonacci number 
    fibonacci_sequence.append(previous_number_2)

    # Calculate next Fibonacci number
    next_number = previous_number_2 + previous_number_1

    # Shift values forward for next loop
    previous_number_2 = previous_number_1
    previous_number_1 = next_number

# Display the result
print("Fibonacci Sequence:", fibonacci_sequence)
