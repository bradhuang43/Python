
# Online Python - IDE, Editor, Compiler, Interpreter


n = int(input('Enter the number: '))

print(f'factor of {n} is:')
print(f'1')

for i in range(2,int(n/2)+1):
 if n % i == 0:
    print(f'{i}')
if n > 1:
  print(f'{n}')
