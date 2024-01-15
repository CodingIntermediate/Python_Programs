str=input('enter a name :')
str=str.casefold()
r=reversed(str)

if list(r)==list(str):
    print('palindrome')
else:
    print('not pali')   