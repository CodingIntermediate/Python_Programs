
l=int(input('enter a limit'))
names=[]
for i in range(l):
    n=input()
    names.append(n)

print('Ascending:',sorted(names))
print('Descending:',sorted(names,reverse=True))