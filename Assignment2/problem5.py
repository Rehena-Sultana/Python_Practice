'''
5. FizzBuzz:
   1 থেকে 50 পর্যন্ত:
   - 3 এর গুণিতক হলে "Fizz"
   - 5 এর গুণিতক হলে "Buzz"
   - দুটোরই গুণিতক হলে "FizzBuzz"
   - অন্যথায় সংখ্যাটা print করো
'''
for i in range(1,51):
    
    if i%3==0 and i%5==0: # check this condition first otherwise fizz or buzz will print instead of fizzbuzz
        print ("FizzBuzz")
    
    elif i%3 ==0:
        print("Fizz")

    elif i%5==0:
        print("Buzz")

    else:
        print(i)

