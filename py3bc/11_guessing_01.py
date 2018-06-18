import random
playAgain = 'y'

while playAgain == 'y':
    rand = random.randint(1, 10)
    while True:
        prompt = 'Guess a number between 1 and 10: '
        guess = input(prompt)
        if int(guess) == rand:
            break
        elif int(guess) > rand:
            print('Too high!')
        else:
            print('Too low')
    playAgain = input('Play again? y/n: ')
