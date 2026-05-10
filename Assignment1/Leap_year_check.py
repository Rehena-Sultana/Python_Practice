'''
2. একটা বছর নাও, Leap Year কিনা বলো
   Rule: (4 দিয়ে ভাগ যায় AND 100 দিয়ে যায় না)
         OR (400 দিয়ে ভাগ যায়)

'''
# let's take a year
year = int(input("Enter the year:"))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year," is leap year")

else:
    print(year, " is not leap year")


