l=int(input('enter a limit'))

if l>1:
    for i in range(2,l):
        if l%i==0:
            print(l,':not prime')
            break
    else:
        print(l,':prime')
else:
    print(l,':not prime')
