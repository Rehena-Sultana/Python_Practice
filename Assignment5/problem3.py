'''
 Lambda দিয়ে:
   - List of dicts sort করো multiple key এ
     (প্রথমে city, তারপর age)
   - map() দিয়ে Celsius list কে
     Fahrenheit এ convert করো
     F = (C × 9/5) + 32
'''
people = [
    {"name": "Rahela",  "city": "Dhaka",      "age": 25},
    {"name": "Karim",   "city": "Chittagong",  "age": 30},
    {"name": "Sumaiya", "city": "Dhaka",       "age": 22},
    {"name": "Tanvir",  "city": "Chittagong",  "age": 25},
]

sorted_people = sorted(people, key=lambda x: (x["city"], x["age"]))

for p in sorted_people:
    print(f"{p['city']:<15} {p['age']}  {p['name']}")

# converting celsius to farenheit
celsius = [0, 10, 20, 30, 37, 40, 100]
farenheit = list(map(lambda c: (c*9/5) + 32, celsius))
print(farenheit)