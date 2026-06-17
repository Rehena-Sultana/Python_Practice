#To change or modify the private data we use setter method that ensures validation
class Person:
    def __init__(self,name,age):
        self.name= name
        self.__age= age # double underscore means private

    #define getter method
    def age_get(self):
        return self.__age
    
    #define setter method
    def age_setter(self,age):
        if age>0:
            self.__age=age
        else:
            print("Age can not be negative")

#object create of Person class
p1= Person("Reha",26)
print(p1.age_get())

p1.age_setter(30) # to alter the private data - setter method is used
print(p1.age_get()) #to access the private data- getter method is used