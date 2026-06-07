'''
একটা Calculator function বানাও:
   - *args নেবে (যেকোনো সংখ্যক number)
   - **kwargs নেবে (operation="sum"/"avg"/"max"/"min")
   - Default operation = "sum"
'''
def calculator(*args, **kwargs): # kwargs is a dictionary,first → the key and  the default value if that key does not exist
    numbers = list(args)

    if not numbers:
        return "Error: no numbers given!"

    operation = kwargs.get("operation", "sum")

    if operation == "sum":
        return sum(numbers)
    elif operation == "avg":
        return sum(numbers) / len(numbers)
    elif operation == "max":
        return max(numbers)
    elif operation == "min":
        return min(numbers)
    else:
        return f"Unknown operation: '{operation}'"



print("Default (sum):", calculator(10, 20, 30, 40, 50))
print("Sum:          ", calculator(10, 20, 30, 40, 50, operation="sum"))
print("Average:      ", calculator(10, 20, 30, 40, 50, operation="avg"))
print("Max:          ", calculator(10, 20, 30, 40, 50, operation="max"))
print("Min:          ", calculator(10, 20, 30, 40, 50, operation="min"))
print("Bad operation:", calculator(10, 20, 30, operation="multiply"))
print("No numbers:   ", calculator())