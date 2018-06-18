prompt = 'What\'s your age?'
age = input(prompt)

if age:
    age = int(age)
    if age >= 21:
        print('enjoy the show')
    elif age >= 18:
        print('Have a wristband')
    else:
        print('too young, sorry')
else:
    print('You need to enter a value...')