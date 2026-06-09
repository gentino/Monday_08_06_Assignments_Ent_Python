'''
This Python program generates and displays a calendar for a specific month and year based on user input. 
The user can enter the month either as a number (e.g., 12) or as a month name (e.g., December). 
The program then converts the input into a valid month number and uses Python’s built-in calendar module to display the full monthly calendar.
'''

import calendar
# MONTH MAPPING DICTIONARY
# Maps month names (string) to their numeric representation
# Example: "january" -> 1
month_mapper = {
    'january': 1,
    'february': 2,
    'march': 3,
    'april': 4,
    'may': 5,
    'june': 6,
    'july': 7,
    'august': 8,
    'september': 9,
    'october': 10,
    'november': 11,
    'december': 12
}

# INPUT SECTION
# Prompt user to enter a valid year and month
# Month can be entered as a number (e.g. 12) or name (e.g. December)
year = int(input("Enter year (e.g. 2026): ").strip())
month_input = input("Enter a month (name or number e.g. 12 or December): ").strip()


# Convert user input into a numeric month value
if month_input.isdigit():
    # If input is numeric, directly convert to integer
    month = int(month_input)
else:
    # Convert month name to lowercase and map to number
    month = month_mapper[month_input.lower()]



# Display the calendar for the selected month and year
print(f"\nThe calendar Output is given below:")
print(calendar.month(year, month))
