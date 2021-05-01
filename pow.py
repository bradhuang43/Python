def pow(a, b):
    f=1
    for i in range (0,b):
        f=f*a    
    return (f)

a = float(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'pow of {a} and {b} is {pow(a, b)}')
