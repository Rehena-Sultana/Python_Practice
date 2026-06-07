'''
একটা Student Management System:
   - Dict এ ৫ জন student এর নাম ও marks রাখো
   - সবার average বের করো
   - Pass ও Fail আলাদা dict এ রাখো
   - সর্বোচ্চ marks কার সেটা বের করো
'''
# let's take a dict
students = {
    "Rahela Begum":  85,
    "Karim Hossain": 42,
    "Sumaiya Akter": 91,
    "Tanvir Ahmed":  36,
    "Nafisa Islam":  67,
}

# computing average
total = sum(students.values())
average = total/ len(students)
print("Average number is:", average)

# creating two dicts for pass and fail students
passed_students = {name:marks for name, marks in students.items() if marks>=50}
failed_students = { name : marks for name, marks in students.items() if marks<50}

print("Passed students are:", passed_students)
print("Failed students are:", failed_students)

# highest mark scorer
topper = max(students, key=students.get)
print(f"Topper: {topper} with {students[topper]} marks")