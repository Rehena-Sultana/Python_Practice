'''
3. নিচের pattern print করো:
        *
       ***
      *****
     *******
    *********
'''

n = 5

for i in range(1, n + 1):

    # space print
    print(" " * (n - i), end="")

    # star print (odd numbers: 1,3,5,7,...)
    print("*" * (2 * i - 1))