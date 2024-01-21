# Pearl Natalia
# The Game of Life


# --- Imports ---
import config
import random
from board_file import intro
from board_file import p1_board
from board_file import p2_board
from career_file import graduation


# --- Introduction ---
intro() 
p1_name = str(input('\n\nPlayer 1 Name: '))
p2_name = str(input('Player 2 Name: '))


# --- Career Path ---
rounds = 0
for i in range(2):
	rounds += 1
	# Player 1
	if rounds % 2 == 1:
		config.player = 1
		config.p1_spot += 1
		print('\n\nPLAYER 1 - ' + p1_name + ':')
		# Player 2
	elif rounds % 2 == 0:
		config.player = 2 
		config.p2_spot += 1
		print('\n\nPLAYER 2 - ' + p2_name + ':')
	graduation()


# --- When 2 Players Are Playing ---
while len(config.players_retired) == 0:
	# To keep track of whose turn it is
	rounds += 1	
	if rounds % 2 == 1:
		config.player = 1
		print('\n\nPLAYER 1:')
	elif rounds % 2 == 0:
		config.player = 2 
		print('\n\nPLAYER 2:')
	
	# Dice
	enter = input('\n\tPress enter to roll the dice: ')
	config.dice = random.randint(1, 10)
	print(enter, '\tYou rolled:', config.dice)

	# Functions of the board
	if config.player == 1:
		p1_board()
	elif config.player == 2:
		p2_board()


# --- When Only 1 Player Is Left ---
# Checking which player is left
if 'player1' in config.players_retired:
	config.player = 2
elif 'player2' in config.players_retired:
	config.player = 1

# Game continues until all player retire
while len(config.players_retired) == 1:
	# Only player 1 plays if not retired
	if config.player == 1:
		print('\n\nPLAYER 1:')
		
		# Dice
		enter = input('\n\tPress enter to roll the dice: ')
		config.dice = random.randint(1, 10)
		print(enter, '\tYou rolled:', config.dice)
		
		p1_board()

	# Only player 2 plays if not retired
	elif config.player == 2:
		print('\n\nPLAYER 2:')

		# Dice	
		enter = input('\n\tPress enter to roll the dice: ')
		dice = random.randint(1, 10)
		print(enter, '\tYou rolled:', dice)

		p2_board()
	

# --- When Both Players Have Retired ---
print('\n' + '-' * 166 + '\n')
print("\nYou've reached the end of the game!")
print('\nPlayer 1 Account Balance: $' + str(config.player1 * 1000) + 'K')
print('Player 2 Account Balance: $' + str(config.player2*1000) + 'K')

# Checking which player won the game based on account balance
if config.player1 > config.player2:
	print('\nPlayer 1 won the Game of Life! Congrats!')
elif config.player1 < config.player2:
	print('\nPlayer 2 won the Game of Life! Congrats!')