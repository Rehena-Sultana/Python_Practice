# multiple classes have same method name

# first class
class Dog:
    def __init__(self,name):
        self.name=name
      
    def sound(self):
        print("Barks")

# second class
class Cat:
    def __init__(self,name):
        self.name=name
    
    def sound(self):
        print("Meow")

#creating objects for every classes
dog1= Dog("a")
cat1= Cat("b")

for animal in (dog1,cat1) :
   animal.sound()