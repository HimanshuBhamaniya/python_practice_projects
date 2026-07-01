import random, sys

print('ROCK','PAPER','SCISSORS')

wins = 0
loses = 0
ties = 0

while True:
    print('%s Wins, %s Loses, %s Ties' %(wins,loses,ties))
    while True:
        print('Enter your move: (r)ock (p)aper (s)cissors or exit')
        player_input = input('>')
        if player_input == 'exit':
            sys.exit()
        if player_input == 'r' or player_input == 'p' or player_input == 's':
            break
        print('Type one of r, p, s, or exit.')
    
    if player_input == 'r':
        print('ROCK versus...')
    elif player_input == 'p':
        print('PAPER versus...')
    elif player_input == 's':
        print('SCISSORS versus...')
    
    move_number = random.randint(1,3)
    if move_number == 1:
        computer_move = 'r'
        print ('ROCK')
    elif move_number == 2:
        computer_move = 'p'
        print('PAPER')
    elif move_number == 3:
        computer_move = 's'
        print('SCISSORS')
    
    if player_input == computer_move:
        print('It is a tie!')
        ties = ties + 1
    elif player_input == 'r' and computer_move == 's':
        print('You win!')
        wins = wins + 1
    elif player_input == 'p' and computer_move == 'r':
        print('You win!')
        wins = wins + 1
    elif player_input == 's' and computer_move == 'p':
        print('You win!')
        wins = wins + 1
    elif player_input == 'r' and computer_move == 'p':
        print('You lose!')
        loses = loses + 1
    elif player_input == 'p' and computer_move == 's':
        print('You lose!')
        loses = loses + 1
    elif player_input == 's' and computer_move == 'r':
        print('You lose!')
        loses = loses + 1
    