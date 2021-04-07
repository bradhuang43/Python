def Factorial(n):
    F=1
    for I in range(2,n+1):
        F=F*I
    return (F)

n=0.5
while type(n) is not int: 
   try: 
      n = input("Please enter a positive integer: ") 
      n = int(n) 
      if n < 0: 
         print("%d is not positive. Try again!/n" % n) 
   except ValueError: 
      print("%s is not an integer. Try again!/n" % n)
      
print(f'Factorial of {n} is {Factorial(n)}')
