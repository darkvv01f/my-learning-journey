name = input('Enter your name:\n')
print('Welcome', name)

age = int(input('Please enter your age:\n'))
Ok = age >= 18

if Ok:
    print('Welcome to the site',name)
    suggested_nickname=(name+str(age))
    print('Suggested_Nickname:',suggested_nickname)
    chosen_nickname=input('Please enter your nickname:\n')
    print('Your nickname is:', chosen_nickname)
    
else:
    print('Error')