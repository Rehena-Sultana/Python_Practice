# hiding data inside the class
class Person:
    def __init__(self,name,age):
        self.name= name
        self.__age= age # double underscore means private

#object create of Person class
p1= Person("Reha",26)
print(p1.name) # output Reha
print(p1.__age) # causes error as it's private