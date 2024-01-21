# House file

# House function
def house():
	# Imports
	import random
	import config

	# Shuffling card deck
	random.shuffle(config.house_cards)
	end_range = len(config.house_cards) -1
	
	# Asking player to randomly pick 2 house cards
	print('\n\tYou landed on the house tile!')
	print('\n\tEnter 2 different numbers between 0 - ' + str(end_range), 'to draw 2 house cards')
	choice1 = int(input('\t\t- 1st number: '))
	choice2 = int(input('\t\t- 2nd number: '))

	choice1 = (config.house_cards[choice1])
	choice2 = (config.house_cards[choice2])

	house_cost1 = 0
	house_red1 = 0
	house_black1 = 0
	house_cost2 = 0
	house_red2 = 0
	house_black2 = 0

	# Assigning cost of house and its 2 possible selling prices
	if choice1 == 'Houseboat':
		house_cost1 = 200
		house_red1 = 180
		house_black1 = 300
	elif choice1 == 'Dream Villa':
		house_cost1 = 300
		house_red1 = 250
		house_black1 = 380
	elif choice1 == 'Island Holiday Home':
		house_cost1 = 600
		house_red1 = 650
		house_black1 = 800
	elif choice1 == 'Cozy Cottage':
		house_cost1 = 150
		house_red1 = 120
		house_black1 = 200
	elif choice1 == 'Family House':
		house_cost1 = 250
		house_red1 = 200
		house_black1 = 300
	elif choice1 == 'Studio Apartment':
		house_cost1 = 100
		house_red1 = 80
		house_black1 = 	150
	elif choice1 == 'Farmhouse':
		house_cost1 = 300
		house_red1 = 250
		house_black1 = 380
	elif choice1 == 'Ranch':
		house_cost1 = 600
		house_red1 = 600
		house_black1 = 750
	elif choice1 == 'Beach Hut':
		house_cost1 = 100
		house_red1 = 80
		house_black1 = 150
	elif choice1 == 'Luxury Apartment':
		house_cost1 = 250
		house_red1 = 200
		house_black1 = 300
	elif choice1 == 'Eco House':
		house_cost1 = 200
		house_red1 = 180
		house_black1 = 300
	elif choice1 == 'Windmill':
		house_cost1 = 350
		house_red1 = 300
		house_black1 = 500
	elif choice1 == 'Teepee':
		house_cost1 = 100
		house_red1 = 80
		house_black1 = 150
	elif choice1 == 'City Penthouse':
		house_cost1 = 600
		house_red1 = 650
		house_black1 = 700
	
	if choice2 == 'Houseboat':
		house_cost2 = 200
		house_red2 = 180
		house_black2 = 300
	elif choice2 == 'Dream Villa':
		house_cost2 = 300
		house_red2 = 250
		house_black2 = 380
	elif choice2 == 'Island Holiday Home':
		house_cost2 = 600
		house_red2 = 650
		house_black2 = 800
	elif choice2 == 'Cozy Cottage':
		house_cost2 = 150
		house_red2 = 120
		house_black2 = 200
	elif choice2 == 'Family House':
		house_cost2 = 250
		house_red2 = 200
		house_black2 = 300
	elif choice2 == 'Studio Apartment':
		house_cost2 = 100
		house_red2 = 80
		house_black2 = 	150
	elif choice2 == 'Farmhouse':
		house_cost2 = 300
		house_red2 = 250
		house_black2 = 380
	elif choice2 == 'Ranch':
		house_cost2 = 600
		house_red2 = 600
		house_black2 = 750
	elif choice2 == 'Beach Hut':
		house_cost2 = 100
		house_red2 = 80
		house_black2 = 150
	elif choice2 == 'Luxury Apartment':
		house_cost2 = 250
		house_red2 = 200
		house_black2 = 300
	elif choice2 == 'Eco House':
		house_cost2 = 200
		house_red2 = 180
		house_black2 = 300
	elif choice2 == 'Windmill':
		house_cost2 = 350
		house_red2 = 300
		house_black2 = 500
	elif choice2 == 'Teepee':
		house_cost2 = 100
		house_red2 = 80
		house_black2 = 150
	elif choice2 == 'City Penthouse':
		house_cost2 = 600
		house_red2 = 650
		house_black2 = 700

	# Displaying the 2 options
	print('\n\tNote: Each house comes with 2 sale prices. At the end of the game, you will spin a spinner to determine what your house sells for.')
	print('\n\tYour options are:\n\t\t- Option 1:\n\t\t ', choice1, '\n\t\t  House Cost: $' + str(house_cost1) + 'K\n\t\t  Sale Price 1: $' + str(house_red1) + 'K\n\t\t  Sale Price 2: $' + str(house_black1) + 'K')
	print('\n\n\t\t- Option 2:\n\t\t ', choice2, '\n\t\t  House Cost: $' + str(house_cost2) + 'K\n\t\t  Sale Price 1: $' + str(house_red2) + 'K\n\t\t  Sale Price 2: $' + str(house_black2) + 'K')
	
	# Asking user which house they want to purchase, or neither
	option = int(input('\n\tEnter the number of the option you want. \n\t*Enter 0 if you choose not to purchase a house. However, there is a chance you may not land on a house tile again later on in the game.*\n\tOption: '))

	debt1 = 0
	debt2 = 0

	# Assigning house, house cost, and 2 possible selling pirces to player's database
	# Player 1:
	if option != 0 and config.player == 1:
		if option == 1:
			config.p1_house.append(choice1)
			config.p1_house_cost.append(house_cost1)
			config.p1_house_red.append(house_red1)
			config.p1_house_black.append(house_black1)
			config.player1 -= house_cost1
			# Removing chosen house from card deck
			# Displaying which house was bought
			config.house_cards.remove(choice1)
			print('\n\tYou just bought a', choice1, 'for $' + str(house_cost1) + 'K !\n\tYour account balance is now: $', str(config.player1) + 'K')


		elif option == 2:
			config.p1_house.append(choice2)
			config.p1_house_cost.append(house_cost2)
			config.p1_house_red.append(house_red2)
			config.p1_house_black.append(house_black2)
			config.player1 -= house_cost2
			# Removing chosen house from card deck
			# Displaying which house was bought
			config.house_cards.remove(choice2)
			print('\n\tYou just bought a', choice2, 'for $' + str(house_cost2) + 'K !\n\tYour account balance is now: $', str(config.player1) + 'K')

		# Notifying player if they are in debt
		if config.player1 < 0:
			debt1 = 0 - config.player1
			print('\tCareful! You are now $' + str(debt1) + 'K in debt!')
	
	# Player 2: (same steps from above repeated)
	elif option != 0 and config.player == 2:
		if option == 1:
			config.p2_house.append(choice1)
			config.p2_house_cost.append(house_cost1)
			config.p2_house_red.append(house_red1)
			config.p2_house_black.append(house_black1)
			config.player2 -= house_cost1
			config.house_cards.remove(choice1)
			print('\n\tYou just bought a', choice1, 'for $' + str(house_cost1) + 'K !\n\tYour account balance is now: $', str(config.player2) + 'K')


		elif option == 2:
			config.p2_house.append(choice2)
			config.p2_house_cost.append(house_cost2)
			config.p2_house_red.append(house_red2)
			config.p2_house_black.append(house_black2)
			config.player2 -= house_cost2
			config.house_cards.remove(choice2)
			print('\n\tYou just bought a', choice2, 'for $' + str(house_cost2) + 'K !\n\tYour account balance is now: $', str(config.player2) + 'K')

		if config.player2 < 0:
			debt2 = 0 - config.player2
			print('\tCareful! You are now $' + str(debt2) + 'K in debt!')
	
	# If player doens't purchase a house
	else:
		print('\n\tYou chose not to purchase a house.')
		