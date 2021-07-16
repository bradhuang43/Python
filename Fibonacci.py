
# Online Python - IDE, Editor, Compiler, Interpreter

def fibonacci(n):
    if n == 1:
      return (0)
    if n == 2:
      return (1)
    pre = 0
    cur = 1
    for i in range (1, n-1):
      next = pre + cur
      pre = cur
      cur = next
    return next
    
n = int(input('Enter a positive integer: '))

print(f'The {n}-th fibonacci number is {fibonacci(n)}')
