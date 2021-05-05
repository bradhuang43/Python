def pow(a, b):
    if b > 0 or b == 0:
        f=1
        for i in range (0,b):
            f=f*a    
        return (f)
    else:
        return (1.0/pow(a,-b))
        
a = float(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'pow of {a} and {b} is {pow(a, b)}')
