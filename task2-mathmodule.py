n=float(input('Enter a number: '))

import math

if n<0:
    print('log and square roots are undifined for negetive number.')
else:
    sqr= math.sqrt(n)
    log= math.log(n)
    sin= math.sin(n)

    print(f'Square root: {sqr}')
    print(f'Logarithm: {log}')
    print(f'sine: {sin}')
