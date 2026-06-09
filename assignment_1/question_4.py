'''
This Python program collects five numbers from the user, stores them in a list, 
calculates their total sum, and then computes the mean (average). 
Finally, it displays the result as a message.
'''


count = 1 
numbers = []
# Input five numbers
while count <=5:
    user_input = int(input(f"Enter  the  value {count} : "))
    numbers.append(user_input)
    count+=1 
        

# Calculate the total
total = sum([num for num in numbers])

# get the count of numbers
count_numbers = len(numbers)

# Calculate the mean
mean = total/count_numbers

# Display the mean
# Display the result as a string
print("The mean of the five numbers is " + str(mean))
