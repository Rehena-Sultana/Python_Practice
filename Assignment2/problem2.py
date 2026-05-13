'''
2. User থেকে numbers নাও যতক্ষণ না
   "done" লেখে — সব সংখ্যার
   sum, average, max, min বের করো
   '''
# let's take an empty list to store the numbers
numbers=[]
sum=0.0


while True:
    user_input = input()
    if user_input.lower()== 'done':
        break
    else:
        numbers.append(float(user_input))
        #sum+= float(user_input)
max = numbers[0]
min = numbers[0]

for i in numbers:
    sum+=i
    if i>max:
        max=i
    if i<min:
        min=i
    
average=sum/len(numbers)

print("the sum of the numbers is: ", sum)
print("the average of the numbers is: ", average)
print("Maximum number is: ",int(max))
print("Minimum number is: ",int(min))

