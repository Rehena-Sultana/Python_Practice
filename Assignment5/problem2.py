'''
Decorator ছাড়া এটা করো:
   - একটা function লিখো যেটা
     অন্য একটা function কে argument হিসেবে নেয়
     এবং সেটা call করার আগে ও পরে
     "Starting..." ও "Done!" print করে
'''
def my_decorator(func):
    print("Starting")
    func()
    print("Done!")

def greet():
    print("Hello World!")

my_decorator(greet)