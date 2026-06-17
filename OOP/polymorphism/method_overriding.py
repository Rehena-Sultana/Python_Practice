# class inheritance

# define parent clsss
class Vehicle:

    def move(self):
        print("Move")

class Car(Vehicle):
    def move(self):
        print("Drive")

class Plane(Vehicle):
    def move(self):
        print("Fly")

v1=Vehicle()
c1= Car()
p1=Plane()

for x in (v1,c1,p1):
    x.move()