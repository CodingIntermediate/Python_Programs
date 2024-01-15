print(' enter numbers 0 to  exit ')
c=0
s=0
num=1

while num!=0:
      num=int(input())
      s=s+num
      c+=1

if c==0:
    print(' Input some number ')    
else:
    print(' avg and sum: ',s/(c-1),s)    


