'''
3. Tuple unpacking দিয়ে:
   - একটা function লিখো যেটা
     নাম ও marks নিয়ে (grade, percentage, status)
     tuple return করে

'''
# function 
def student_result(name, marks):

    # percentage
    percentage = marks

    # grade
    if marks >= 80:
        grade = "A+"

    elif marks >= 70:
        grade = "A"

    elif marks >= 60:
        grade = "B"

    elif marks >= 50:
        grade = "C"

    else:
        grade = "F"

    # status
    status = "Pass" if marks >= 50 else "Fail"

    # tuple return
    return (grade, percentage, status)


# function call
result = student_result("Rehena", 95)

# tuple unpacking
grade, percentage, status = result

print("Grade =", grade)
print("Percentage =", percentage)
print("Status =", status)