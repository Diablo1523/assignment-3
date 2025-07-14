n=int(input('Enter a number: '))

def factorial(n):

    if  n<2:
        return 1
    else:
        return n * factorial(n-1)

if n >= 0:
    res = factorial(n)
    print(res)
else:
    print('Please enter a positive integer.')