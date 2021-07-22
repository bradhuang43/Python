
# Online Python - IDE, Editor, Compiler, Interpreter

def dec2bin(a):
    bin = ''
    while a > 0:
        bin = str(a%2) + bin
        a = int(a / 2)
    
    return bin

a = int(input('Enter the number: '))

print(f'Binary of {a} is {dec2bin(a)}')
