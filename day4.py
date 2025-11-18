names=['name1','name2','name3','name4','name5']
name=input('Enter your name:')
while name not in names:
    print('Error')
    name=input('Enter your name:')
print('Success')