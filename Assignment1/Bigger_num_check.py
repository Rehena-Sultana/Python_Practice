"""
1. দুটো সংখ্যা নাও।
   - বড়টা print করো (ternary দিয়ে)
   - দুটোর মধ্যে যেটা 3 ও 5 উভয়ের গুণিতক সেটা বলো
"""

# let's take two numbers
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

# use the ternary operator
bigger = num1 if num1 > num2 else num2
print("The bigger number is:", bigger)

# check multiples of 3 and 5
if num1 % 3 == 0 and num1 % 5 == 0:
    print(num1, "is divisible by both 3 and 5")

if num2 % 3 == 0 and num2 % 5 == 0:
    print(num2, "is divisible by both 3 and 5")