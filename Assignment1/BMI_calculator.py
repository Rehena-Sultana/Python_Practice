'''
 BMI Calculator:
   - weight ও height নাও
   - BMI = weight / height²
   - Underweight / Normal / Overweight / Obese বলো
   '''
# taking weight and height
weight = float(input("Enter the weight is: "))
height = float(input("Enter the height is: "))

BMI= weight / (height**2)

# BMI category check
if (BMI<18.5):
    print("Category : Underweight")

elif (BMI<25):
    print("Category : Normal")

elif (BMI<30):
    print("Category : Overweight")

else:
    print("Category : Obese")