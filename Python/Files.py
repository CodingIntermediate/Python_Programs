f=open('f.txt','w')
f.write('Hello world\n Hi\n Hi\nBalance')
f.close()

f=open('f.txt','r')
print(f.read(2))
f.close()

f=open('f.txt','r')
print(f.readline(2))
f.close()

f=open('f.txt','a')
f.write('Woops')
f.close()

f=open('f.txt','w')
f.write('Woops')
f.close()