# Retirement function

def retirement():
	import config
	import random

	# FIRST TO RETIRE
	config.players_retired.append('player' + str(config.player))
	print('\n\tRETIREMENT:')

	if len(config.players_retired) == 1:
		print('\tCongratulations, you are the first player to retire! For this, you will receive a $200K compensation!')
		if config.player == 1:
			config.player1 += 200
		elif config.player == 2:
			config.player2 += 200
	
	elif len(config.players_retired) == 2:
		print('\n\tCongratulations, you finally retired! Unfortunately, you were NOT the first player to retire, and so you will only receive a $100K compensation.')
		if config.player == 1:
			config.player1 += 100
		elif config.player == 2:
			config.player2 += 100
	
	print('\n\tBelow will be calculated your compensation and earnings for your:\n\t\t- Action Card(s) \n\t\t- Trivia Card(s) \n\t\t- Kid(s) \n\t\t- House(s)')

	# COMPENSATION FOR KIDS
	print('\n\tKIDS:')
	if config.player == 1:
		compensation_kids = config.p1_kids * 50
		config.player1 += compensation_kids
		print('\tYou got a $' + str(compensation_kids) + 'K compensation for all of your children.')
	
	elif config.player == 2:
		compensation_kids = config.p2_kids * 50
		config.player2 += compensation_kids
		print('\n\tYou got a $' + str(compensation_kids) + 'K compensation for all of your children.')

	# COMPENSATION FOR ACTION CARDS
	print('\n\tACTION/TRIVIA CARDS: ')
	if config.player == 1:
		compensation_cards = config.p1_cards * 10
		config.player1 += compensation_cards
		print('\tYou got a $' + str(compensation_cards) + 'K compensation for all of your action/trivia cards.') 
	
	elif config.player == 2:
		compensation_cards = config.p2_cards * 10
		config.player2 += compensation_cards
		print('\tYou got a $' + str(compensation_cards) + 'K compensation for all of your action/trivia cards.') 

	# HOUSE SELLING PRICE
	print('\n\tHOUSE SELLING PRICE:')
	print('\tYou will spin the spinner. Your house will sell for a specific price based on the colour the spinner lands on')

	if config.player == 1:
		index = 0
		for a in config.p1_house:
			print('\n\t\t' + a + ':')

			print('\t\tBlack - $' + str(config.p1_house_black[index]) + 'K')
			print('\t\tRed - $' + str(config.p1_house_red[index]) + 'K')

			enter = input('\t\tPress enter to spin the spinner: ')

			number = random.randint(1, 10)
			if number % 2 == 0:
				print('\t\tYou landed on black.')
				config.player1 += config.p1_house_black[index]
				print('\t\tYour house sold for $' + str(config.p1_house_black[index]) + 'K !')

			elif number % 2 == 1:
				print('\t\tYou landed on red.')
				config.player1 += config.p1_house_red[index]
				print('\t\tYour house sold for $' + str(config.p1_house_red[index]) + 'K !')

			index += 1
	
	elif config.player == 2:
		index = 0
		for a in config.p2_house:
			print('\n\t\t' + a + ':')

			print('\t\tBlack - $' + str(config.p2_house_black[index]) + 'K')
			print('\t\tRed - $' + str(config.p2_house_red[index]) + 'K')

			enter = input('\t\tPress enter to spin the spinner: ')

			number = random.randint(1, 10)
			if number % 2 == 0:
				print('\t\tYou landed on black.')
				config.player2 += config.p2_house_black[index]
				print('\t\tYour house sold for $' + str(config.p2_house_black[index]) + 'K !')

			elif number % 2 == 1:
				print('\t\tYou landed on red.')
				config.player2 += config.p2_house_red[index]
				print('\t\tYour house sold for $' + str(config.p2_house_red[index]) + 'K !')

			index += 1

	return enter