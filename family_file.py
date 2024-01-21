# Family file

# kids spinner function
def kids_spinner():
	# Imports
	import random
	import config

	# Explaining rules of kids spinner
	print('\n\tSTOP: You reached the kids spinner! You will spin the spinner to have kids. \n\tThe number the spinner lands on determines how many kids you will have:')
	print('\t\t1 = 0 children\n\t\t2 - 4 = 1 child\n\t\t5 - 7 = 2 children\n\t\t8 - 10 = 3 children')
	
	# Spinner
	enter = input('\n\tPress enter to spin the spinner! ')
	number = random.randint(1, 10)
	print('\tYou landed on a:', number)

	# Determining how many kids player has based on number spinner lands on
	# Player 1:
	if config.player == 1:
		if number == 1:
			config.p1_kids = 0
		elif number > 1 and number < 5:
			config.p1_kids = 1
		elif number > 4 and number < 8:
			config.p1_kids = 2
		elif number > 7:
			config.p1_kids = 3
		
		if config.p1_kids > 0:
			print('\n\tCongratulations! You just had', config.p1_kids, 'kid(s)!')
			print('\tYou will receive a 50k/child compensation when you retire.')
		else:
			print('\n\tYou had no kids.')


	# Player 2:
	elif config.player == 2:
		if number == 1:
			config.p2_kids = 0
		elif number > 1 and number < 5:
			config.p2_kids = 1
		elif number > 4 and number < 8:
			config.p2_kids = 2
		elif number > 7:
			config.p2_kids = 3
		
		if config.p2_kids > 0:
			print('\n\tCongratulations! You just had', config.p2_kids, 'kid(s)!')
			print('\tYou will receive a 50k/child compensation when you retire.')
		else:
			print('\n\tYou had no kids.')
	
	return enter


# Child function
def child(): 
	# Imports
	import config
	import random

	# Description of child tile
	print('\n\tYou landed on the child tile!')
	print('\tCongratulations! You just had a baby! Spin the spinner to determine the gender!')
	
	# Spinner
	enter = input('\n\tPress enter to spin the spinner! ')
	number = random.randint(1, 10)

	# Determining gender based on number spinner lands open
	# Player 1:
	if config.player == 1:
		if number % 2 == 0:
			print("\tIt's a baby girl!")
		elif number % 2 == 1:
			print("\tIt's a baby boy!")
		config.p1_kids += 1
	
	# Player 2:
	elif config.player == 2:
		if number % 2 == 0:
			print("\tIt's a baby girl!")
		elif number % 2 == 1:
			print("\tIt's a baby boy!")
		config.p2_kids += 1
	
	print('\tYou will receive a 50k/child compensation when you retire.')
	return enter


# Marriage function
def marriage():
	# Imports
	import random
	import config
	
	# Explaining rules of marriage tile
	print("\n\tSTOP: You reached the marriage tile! \n\tCongratulations! You're getting maried!")
	print('\n\tYou will receive either a $50k or $100k wedding gift from the other player.')
	print('\t\tOdd Number - $50k\n\t\tEven Number - $100k')
	
	# Spinner
	enter = input('\n\tPress enter to spin the spinner: ')
	number = random.randint(1, 10)
	print('\tYou landed on:', number)

	# Determining value of wedding present based on number spinner lands on
	# Player 1:
	if config.player == 1:
		if number % 2 == 1:
			print('\tYou received $50k!')
			config.player1 += 50
			config.player2 -= 50
		elif number % 2 == 0:
			print('\tYou received $100k!')
			config.player1 += 100
			config.player2 -= 100

	# Player 2
	elif config.player == 2:
		if number % 2 == 1:
			print('\tYou received $50k!')
			config.player2 += 50
			config.player1 -= 50
		elif number % 2 == 0:
			print('\tYou received $100k!')
			config.player2 += 100
			config.player1 -= 100
	
	# Displaying account balance of each player
	# Notifying if a player is in debt
	print("\n\tPlayer 1's account balance: $" + str(config.player1) + 'k')
	if config.player1 < 0:
		debt = 0 - config.player1
		print('\tCareful! Player 1 is now $' + str(debt) + 'K in debt!')
	
	print("\tPlayer 2's account balance: $" + str(config.player2) + 'k')
	if config.player2 < 0:
		debt = 0 - config.player2
		print('\tCareful! Player 2 is now $' + str(debt) + 'K in debt!')
	
	return enter
