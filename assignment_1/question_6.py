'''
This Python program generates and displays multiplication tables for numbers from 2 to 12.
For each base number, it prints a neatly formatted table showing its multiplication results from 1 to 12. 
The program uses nested loops to handle both the base numbers and their multipliers.
'''

# Loop through base numbers from 2 to 12 (multiplication tables)
for base_number in range(2, 13):
    
    # Print a separator line for better readability
    print("_" * 30)
    
    # Display which multiplication table is being shown
    print(f"{base_number} Multiplication Table:")
    
    # Another separator for visual clarity
    print("=" * 30)
    
    # Loop through multipliers from 1 to 12
    for multiplier in range(1, 13):
        
        # Calculate the product of base number and multiplier
        result = base_number * multiplier
        
        # Display the formatted multiplication statement
        print(f"{base_number} * {multiplier} = {result}")
