Online Python - IDE, Editor, Compiler, Interpreter

def readyfortiger(a):
    if a <= 0:
        return ('you got to be kiding')
    elif a< 100:
        return ('tiger has to wait')
    elif a < 400:
        return ('tiger can use this kid')
    else:
        return ('there\'s no kid that can be this heavy')

a=float(input('Enter the bad kids weight in lbs: '))

print(f'{readyfortiger(a)}')
