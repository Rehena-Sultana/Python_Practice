# To access private data, we use getter method
class Person:
    def __init__(self,name,age):
        self.name= name
        self.__age= age # double underscore means private

    #define getter method
    def age_get(self):
        return self.__age
        
#object create of Person class
p1= Person("Reha",26)
print(p1.age_get()) # now 26 will print