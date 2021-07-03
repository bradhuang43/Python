
# Online Python - IDE, Editor, Compiler, Interpreter

def min2(a, b):
    if a < b:
        return a
    else:
        return b

def min3(a, b, c):
    d = min2(a, b)
    print(f'd is {d}')
    return min2(d, c)
   
a = (input('Enter 1st number: '))
b = (input('Enter 2nd number: '))
c = (input('Enter 3rd number: '))

print(f'min of all is {min3(a, b, c)}')
