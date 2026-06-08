# Inheritance happens level by level.
# current class inherits immediate previous class

# create class1: person

class Person:

    def __init__(self, name):
        self.name = name
    def introduce(self):
        print("Name: ", self.name)


# create class2: doctor that inherits class1
class Doctor(Person):

    def __init__(self, name, hospital):
        super().__init__(name)
        self.hospital = hospital

    def hospital_info(self):
        print(f"{self.name} works at {self.hospital}")


# create class 3 that inherits class2
class Surgeon(Doctor):
    def __init__(self,name,hospital,specialist):
        super().__init__(name,hospital)
        self.specialist = specialist

    def surgery(self):
        print(f"{self.name} is special surgeon on {self.specialist}")

# cretae an onject of surgeon class
s= Surgeon("Hassan","Appolo hospital","Heart")
s.introduce()
s.hospital_info()
s.surgery()