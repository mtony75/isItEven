#functions
def isItEven():
    usrNumber = input('Enter a number: ')
    if type(int(usrNumber)).__name__ == 'int':
        numberMod = int(usrNumber) % 2
        if numberMod == 0:
            print('Your number is even')
        elif numberMod == 1:
            print('Your number is odd')
        else:
            print('Not a number')

def areTheyDivisible():
    print('I am going to ask you for two numbers.')
    print('Thin I will see if they are divisible')
    print('')

    firstNumber = input('Please enter a number: ')
    secondNumber = input('Please enter a second number: ')

    try:

        if type(int(firstNumber)).__name__ == 'int':
            print('First number is valid.')
#    else:
#        print('First number is invalid.')
#        print('Goodbye')
#        return
    except ValueError:
        print('Error: {} Is an invalid arguement.'.format(firstNumber))
        print('Error: {} Is of type {}. '.format(firstNumber, type(firstNumber).__name__))
        return

    try:
        if type(int(secondNumber)).__name__ =='int':
            print('Second number is valid.')

    except ValueError:
        print('Error: {} Is an invalid arguement.'.format(secondNumber))
        print('Error: {} Is of type {}. '.format(secondNumber, type(secondNumber).__name__))
        return
#    else:
#        print('Second number is invalid.')
#        print('Goodbye')
#        return

    if int(firstNumber) % int(secondNumber) == 0:
        print('{} is divisible by {}'.format(firstNumber, secondNumber))
        return
    else:
        print('The numbers are not divisible.')
        return


#main Section

print('Welcome to is even.')
print('Give me a number and I will tell')
print('you if the number is even.')

print('')
print('Please make a selection')
print('1. Is it even')
print('2. Is it divisible')
print('')
usrInput = input('Enter Selection: ')

if int(usrInput) == 1:
    isItEven()
elif int(usrInput) == 2:
    areTheyDivisible()
else:
    print('Not a vaild response. Goodbye!')