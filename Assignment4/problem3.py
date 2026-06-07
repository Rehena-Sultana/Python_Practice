'''
Set দিয়ে:
   - দুটো class এর student list নাও
   - দুই class এই আছে এমন student বের করো
   - শুধু Class A তে আছে এমন বের করো
   - দুই class মিলিয়ে মোট unique student কতজন
'''
class_a = {"Rahela", "Karim", "Sumaiya", "Tanvir", "Nafisa"}
class_b = {"Sumaiya", "Nafisa", "Arif", "Mim", "Sakib"}

# students who exists in both class
common_students = class_a & class_b
print ("Common students are:",common_students)

# students only exists in class a not in b
only_a = class_a -class_b
print ("Students from belonging class_a are:", only_a)

#total unique students
total_unique_students = class_a | class_b
print(f" Total unique {len(total_unique_students)} students are: {total_unique_students} ")