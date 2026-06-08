import calendar

year = int(input("Enter a year (e.g 2026)").strip())

start_month = input('Enter the start month (eg. 6 or June)').strip() 
end_month =  input('Enter the start month (eg. 9 or September)').strip()


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


#convert user input into numeric  logic

if start_month.isdigit():
    start_month = int(start_month)
else:
    start_month = month_mapper[start_month]   
    

if end_month.isdigit():
    end_month = int(end_month)
else:
    end_month = month_mapper[end_month]    
    

# Create a calendar object
cal = calendar.TextCalendar()

# end_month + 1 ensures the ending month is included
for month in range(start_month, end_month + 1):
    cal.prmonth(year, month)
    print("-"*20 )  # Visual separator between months
