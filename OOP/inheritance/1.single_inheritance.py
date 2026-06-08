# single inheritance : One parent → one child
class Employee:

    def __init__(self, name,salary):
        self.name = name
        self.salary = salary
    
    def show_info(self):
        print("Employee name is:",self.name)
        print("Salary is:", self.salary)

# define another class that inherits the characteristics of employee class
class Developer(Employee):

    def __init__(self,name,salary,language):
        super().__init__(name,salary)
        self.language=language
    
    def code(self):
        print(f"{self.name} writes code in {self.language}")

#create an object of developer class 
d1 = Developer("Mina", 50000, "Python")
d1.show_info()
d1.code()
