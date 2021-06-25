
# Online Python - IDE, Editor, Compiler, Interpreter


n = int(input('Enter the number: '))
if n == 1:
 print(f'Neither Composite nor Prime')
 exit()

Composite = False

for i in range(2,int(n/2)+1):
 if n % i == 0:
  Composite = True
  break


if Composite:
 print(f'Composite')
else:
 print(f'Prime')
