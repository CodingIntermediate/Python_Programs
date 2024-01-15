def fact(n):
   if n==1:
      f=1
   else:
      f=n*fact(n-1)    
   return f

n=int(input('enter a limit'))
print('Fact:',fact(n))

