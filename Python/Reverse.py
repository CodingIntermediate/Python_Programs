l=int(input('enter the number'))

rem=0
rev=0

while l>0:
    rem=l%10
    rev=(rev*10)+rem
    l=l//10
print('Entered numbers in reverse=',rev)    