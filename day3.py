name = input('Enter your name:\n')
print('Welcome', name)

age = int(input('Please enter your age:\n'))
Ok = 75>= age >= 18

if Ok:
    print('Age verified',name)
    suggested_nickname=(name+str(age))
    print('Suggested login:',suggested_nickname)
    chosen_nickname=input('Please enter your login:\n')
    print('Your login is:', chosen_nickname)
    password=input('Please create a password:\n')
    
    print ('You are too old')
    password1=input('Please confirm your password:\n')
    while password1!=password:
        print('Incorrect password')
        password1=input('Please confirm your password:\n')
    print('Confirmed')
elif age>75:
    print ('You are too old')
    
else:
    print('Age was not verified')