''' 1. একটা student mark list তৈরি করো।
   - সব marks এর average বের করো
   - সর্বোচ্চ ও সর্বনিম্ন mark কার সেটা বের করো
   - Pass (>=50) ও Fail এর list আলাদা করো
     (list comprehension দিয়ে)
'''
# create a student mark list

students = [
    {"name": "Rahim", "mark": 85},
    {"name": "Karim", "mark": 42},
    {"name": "Nila", "mark": 76},
    {"name": "Sadia", "mark": 91},
    {"name": "Hasan", "mark": 48}
]

# total marks
total_marks = 0

for s in students:
    total_marks += s["mark"]

# average
average = total_marks / len(students)

print("Average Mark =", average)

# highest and lowest
max_mark = max(s["mark"] for s in students)
min_mark = min(s["mark"] for s in students)

topper = [s for s in students if s["mark"] == max_mark][0]
lowest = [s for s in students if s["mark"] == min_mark][0]

print(f"Highest mark: {topper['name']} → {max_mark}")
print(f"Lowest mark: {lowest['name']} → {min_mark}")

# pass and fail list
pass_students = [s["name"] for s in students if s["mark"] >= 50]
fail_students = [s["name"] for s in students if s["mark"] < 50]

print("Pass Students =", pass_students)
print("Fail Students =", fail_students)
