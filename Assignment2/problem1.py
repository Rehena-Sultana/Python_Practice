'''
1. 1 থেকে 100 এর মধ্যে:
   - সব জোড় সংখ্যার যোগফল বের করো
   - সব বিজোড় সংখ্যা print করো
   - 3 ও 7 উভয়ের গুণিতক সংখ্যা গুলো print করো
'''
# sum of even numbers between 1 to 100

sum=0
print("Odd numbers are:")
for i in range(1, 101):
    if(i%2==0):
        sum+=i
    
    else:
        print(i, end = ' ')

print("\nThe sum of even number from 1 to 100 is: ", sum)
print("\nnumbers divisible by 3 and 7 are:")
for i in range(1, 100):
    if(i%3==0 and i%7==0):
        print(i, end=' ')