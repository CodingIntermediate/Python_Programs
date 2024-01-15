l=int(input('enter a limit'))

num=[]
for i in range(l):
    n=int(input())
    num.append(n)
print('Before sorting:',num)    

for i in range(l):
    for j in range(i,l):
        if num[i]<num[j]:
            t=num[i]
            num[i]=num[j]
            num[j]=t
print('Dscending:',num)   


for i in range(l):
    for j in range(i,l):
        if num[i]>num[j]:
            t=num[i]
            num[i]=num[j]
            num[j]=t
print('Ascending:',num)  