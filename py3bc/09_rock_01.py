from random import randint

print('Welcome!')

prompt_u1 = 'Enter P1 choice: '
p1_wins = 'Player 1 wins!'
p2_wins = 'Player 2 wins!'

p1_choice = input(prompt_u1).lower()
computer = randint(0,2)
if computer == 0:
    computer = 'rock'
elif computer == 1:
    computer = 'paper'
else:
    computer = 'scissors'


p2_choice = computer
print(f'The computer picked {computer}')

# paper beats rock
# rock beats scissors
# scissors beats paper

if (p1_choice == 'paper' and p2_choice == 'rock') or (p1_choice == 'rock' and p2_choice == 'scissors') or (p1_choice == 'scissors' and p2_choice == 'paper'):
    print(p1_wins)
elif p1_choice == p2_choice:
    print('draw')
else:
    print(p2_wins)