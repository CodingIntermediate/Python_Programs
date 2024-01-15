def add(x,y):
    print(x+y)
def sub(x,y):
    print(x-y)
def mul(x,y):
    print(x*y)
def div(x,y):
    print(x/y)

a=int(input('enter a number : '))
b=int(input())

op=input('enter a the operation : ')

if '+'==op:
    add(a,b)
if '-'==op:
    sub(a,b)
if '*'==op:
    mul(a,b)
if '/'==op:
    div(a,b)
else:
    print('        Terminaation failed ')