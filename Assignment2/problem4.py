'''
4. List comprehension দিয়ে:
   - 1 থেকে 50 এর মধ্যে সব prime number এর list
   - একটা sentence এর প্রতিটা word এর length এর list
     "Python is awesome language"
'''

prime_number = [n for n in range(2, 51) if all(n % i != 0 for i in range(2, n))]

print("The list of the prime numbers from 1 to 50 is:", prime_number)

sentence =  "Python is awesome language"
print("Word length of the sentence is:", [ len(word) for word in sentence.split()])