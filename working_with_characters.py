str=input('enter a characters: ')
ch=str[0]
if ch.isalnum():
    print('It is alphabet or numeric character')
    if ch.isalpha():
        print('It is an alphabet')
        if ch.isupper():
            print('it is capital letter')
        else:
            print('it is a lower letter')
    else:
        print('It is numeric digit')
elif ch.isspace():
    print('it is a space')
else:
    print('it may be a special character')

