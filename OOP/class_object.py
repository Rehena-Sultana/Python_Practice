#define a person class
class Person:
    #define constructor, called during obj creation
    def __init__(self, name, age):#self is used to represent the obj.object নিজের data এবং method access করতে self ব্যবহার করে।
        self.name= name
        self.age = age
    
    # method
    def introduce(self):
        return f"I'm {self.name} and I'm {self.age} years old."

#object create
person1 = Person("A",10)
person2 = Person("B",20)

print(person1.introduce())
print(person2.introduce())
