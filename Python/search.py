s=[2,4,3,5,8]

x=int(input('enter the number to search'))
f=0
for i in range(len(s)):
    if s[i]==x:
       f=1
       break

if f==1:
    print('found ',i+1,' position')
else:
    print('not found')    


