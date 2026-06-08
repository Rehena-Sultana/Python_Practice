#One child class inherits from multiple parent classes
 
# parent class1: student
class Student:

    def __init__(self, university):
        self.university = university

    def student_info(self):
        print("Studies at:",self.university)

# parent class2: Employee
class Employee:
    def __init__(self,salary):
        self.salary = salary

    def earning(self):
        print("Earns at: ",self.salary)


# child class that inherits parent class 1 & 2
class TA(Student,Employee):
    def __init__(self,university,salary,course_name):
        Student.__init__(self, university)
        Employee.__init__(self,salary)
        self.course_name = course_name
    
    def course(self):
        print("Teaches at: ",self.course_name)


# create an object of child class
ta = TA('CUET',10000,'Python')
ta.course()
ta.student_info()
ta.earning()

