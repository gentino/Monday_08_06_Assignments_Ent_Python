'''
This Python program simulates a simple job application processing system. It collects applicant information (name, age, and gender), 
filters applicants based on age requirements, 
assigns qualified applicants to different departments based on specific rules, and then displays both the accepted and rejected applicants.
'''


# list to store rejected applicants
rejected = []

# list to temporarily store all applicants before sorting
applicants = []

# dictionary to store departments and their workers
departments = {
    'Engineering': [],
    'Admin': [],
    'Customer Care': [],
    'Security': [],
}

# -----------------------------
# COLLECTING APPLICANTS
# -----------------------------
while True:
    
    # get applicant name
    name = input("Enter a name or type 'stop' to finish: ").strip()
    
    # stop condition
    if name == 'stop':
        break
    
    # get age and convert to number
    age = int(input("how old are you ?: "))
    
    # get gender
    gender = input("What's your gender (Male/Female): ").strip()

    # store applicant as a dictionary (one person record)
    new_applicants = {
        'name': name,
        'age': age,
        'gender': gender
    }

    # add to applicants list
    applicants.append(new_applicants)

    print('_' * 37)


# -----------------------------
# SORTING APPLICANTS
# -----------------------------
for person in applicants:
    
    name = person["name"]
    gender = person["gender"]
    age = person["age"]

    # verifying applicants age  (criteria accepts those 18 and above and below 50 )
    if age < 18 or age > 50:
        rejected.append(person)
        continue  # skip further processing

    # assign department based on rules
    if gender.lower() == 'male':
        if age < 25:
            dept = 'Customer Care'
        elif age < 45:
            dept = 'Engineering'
        else:
            dept = 'Security'
    else:
        if age < 31:
            dept = 'Customer Care'
        else:
            dept = 'Admin'

    # store in correct department
    departments[dept].append({
        "name": name,
        "gender": gender,
        "age": age,
        "department": dept
    })


# -----------------------------
# DISPLAY DEPARTMENTS
# -----------------------------
for dept, people in departments.items():
    
    # print department name properly
    print(f"\n{dept.upper()}:")

    for p in people:
        print(p["name"], p["gender"], p["age"], p["department"])


# -----------------------------
# DISPLAY REJECTED APPLICANTS
# -----------------------------
print("\nREJECTED APPLICANTS:")

for r in rejected:
    print(r["name"], r["gender"], r["age"])
