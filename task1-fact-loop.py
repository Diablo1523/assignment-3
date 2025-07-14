n=int(input('Enter the number: '))
fact=1

for i in range(1,n+1):
    fact=fact*i

if n >= 0:
    res=fact
    print(res)
else:
    print('Please enter a positive integer.')