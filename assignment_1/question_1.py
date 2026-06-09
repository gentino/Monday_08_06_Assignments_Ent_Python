'''
This Python program prompts the user to enter their name using the input() function. 
The .strip() method is used to remove any leading or trailing spaces from the user's input. 
After receiving the name, the program displays a personalized greeting message using an f-string. 
The output greets the user with "Good Morning" followed by their name and asks how they are doing.
'''
#gets user name input
name = input("Whats your name ?: ").strip() 
# displays   user's name with greetings
print(f'Good Morning  {name}. How are you doing?') 
