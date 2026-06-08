
# FIBONACCI SEQUENCE GENERATOR
# This program generates the first 'n' Fibonacci numbers

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