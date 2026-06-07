'''
Recursion দিয়ে:
   - Power function: power(base, exp)
   - Sum of digits: sum_digits(1234) → 10
   - Palindrome check: is_palindrome("racecar")
'''
def power(base, exp):
    if exp == 0:          # base case — anything to the power 0 = 1
        return 1
    return base * power(base, exp - 1)


print(power(2, 10))   # 1024

def sum_digits(n):
    if n < 10:            # base case — single digit, return as is
        return n
    return (n % 10) + sum_digits(n // 10)


print(sum_digits(1234))   # 10

def is_palindrome(s):
    if len(s) <= 1:              # base case — 0 or 1 letter = palindrome
        return True
    if s[0] != s[-1]:            # first and last letter do not match
        return False
    return is_palindrome(s[1:-1])  # check the middle part


print(is_palindrome("racecar"))  # True