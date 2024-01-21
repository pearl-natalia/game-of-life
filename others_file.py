# Action and trivia fule

# Action function
def action():
	# Imports
	import config
	import random
	print('\n\tYou landed on an action tile! ')

	# Assigning randomized values to variables
	pay_amt = random.randrange(10, 110, 10 )
	donation = random.randrange(10, 110, 10)
	steal = random.randrange(0, 120, 20)
	child_fee = random.randrange(0, 120, 5)
	lottery = random.randrange(0, 120, 20)
	
	# Action cards
	action_cards = (
		['Pay the other player $' + str(pay_amt) + 'K.' ],
		['Donate $' + str(donation) + 'K to charity.'],
		['Take $' + str(steal) + 'K from the other player.'],
		["Give up one of your kids for adoption. If you don't have a child, pay the bank $" + str(child_fee) + 'K.'],
		['You won $' + str(lottery) + 'K from the lottery!'])


	# Randomly picking a action card
	chosen_action = random.choice(action_cards)
	enter = input('\n\tPress enter to randomly draw an action card: ')
	print(enter, '\t', chosen_action)

	# Displaying and performing action based on action card
	# Player 1:
	if config.player == 1:
		if chosen_action == action_cards[0]:
			config.player1 -= pay_amt
			config.player2 += pay_amt
			print('\n\tPlayer 1: -$' + str(pay_amt) + 'K.')
			print('\tPlayer 2: +$' + str(pay_amt) + 'K.')
		elif chosen_action == action_cards[1]:
			config.player1 -= donation
			print('\n\tPlayer 1: -$' + str(donation) + 'K.')
		elif chosen_action == action_cards[2]:
			config.player1 += steal
			config.player2 -= steal
			print('\n\tPlayer 1: +$' + str(steal) + 'K.')
			print('\tPlayer 2: -$' + str(steal) + 'K.')
		elif chosen_action == action_cards[3]:
			if config.p1_kids > 0:
				print('\n\tYou have up one child for adoption.')
				config.p1_kids -= 1
			else:
				print('\n\tYou have no kids, so you will pay the bank $' + str(child_fee) + 'K.')
				config.player1 -= child_fee
				print('\tAccount Balance: $' + str(config.player2) + 'K')
		elif chosen_action == action_cards[4]:
			config.player1 += lottery
			print('\n\tPlayer 1: +$' + str(lottery) + 'K.')
		config.p1_cards += 1

	# Player 2:
	elif config.player == 2:
		if chosen_action == action_cards[0]:
			config.player2 -= pay_amt
			config.player1 += pay_amt
			print('\n\tPlayer 2: -$' + str(pay_amt) + 'K.')
			print('\tPlayer 1: +$' + str(pay_amt) + 'K.')
		elif chosen_action == action_cards[1]:
			config.player2 -= donation
			print('\n\tPlayer 2: -$' + str(donation) + 'K.')
		elif chosen_action == action_cards[2]:
			config.player2 += steal
			config.player1 -= steal
			print('\n\tPlayer 2: +$' + str(steal) + 'K.')
			print('\tPlayer 1: -$' + str(steal) + 'K.')
		elif chosen_action == action_cards[3]:
			if config.p2_kids > 0:
				config.p2_kids -= 1
				print('\n\tYou have up one child for adoption.')
				print('\tYou now have', config.p2_kids + '.')
			else:
				print('\n\tYou have no kids, so you will pay the bank $' + str(child_fee) + 'K.')
				config.player2 -= child_fee
				print('\tAccount Balance: $' + str(config.player2) + 'K')
		elif chosen_action == action_cards[4]:
			config.player2 += lottery
			print('\n\tPlayer 2: +$' + str(lottery) + 'K.')
		config.p2_cards += 1


# Trivia function
def trivia():
	# Imports
	import math
	import random
	import config
	
	# Displaying rules for answering trivia questions
	print('\n\tYou landed on trivia! Answer the question correctly to earn $50K! \n\tPlease only enter numbers and no units in your answers. \n\tAlways round to 2 decimal places if necessary. \n\tIf the answer is a whole number, write it as a float (example: 9 → 9.0)')

	# Assigning random values to variables
	radius = random.randint(1, 10)
	day = random.randint(5, 30)
	speed = random.randint(40, 120)
	hours = random.randint(10, 30)
	length = random.randint(5, 15)
	animal1 = random.randint(5, 10)
	animal2 = random.randint(5, 10)
	quarters = random.randint(2, 30)
	dimes = random.randint(2, 50)
	nickels = random.randint(2, 60)
	side_length = random.randint(1, 10)
	sides = random.randint(4, 20)
	cups = random.randint(20, 50)
	pears = random.randint(1, 12)
	grams = random.randrange(150, 250, 10)

	# Trivia questions
	questions = [
		[f"What is the circumference of a circle with a radius of {radius} cm?", str(round(math.pi * radius *2, 2)) + 'cm'],

		[f"How many minutes are in {day} days?", str(float(1440 * day))],

		[f"If a car travels at {speed}km/h for {hours} hours, how many km does the car travel?", str(float(speed * hours))],

		[f"A square has a side length of {length} on all sides. \n\tWhat's the distance of one corner of the square to its opposite? \n\tHint: solve for the hypotenuse.", str(round((length**2 + length **2)**0.5, 2))],

		[f"If Emily has {animal1} horses and {animal2} flamingos, how many legs are there in total? \n\tHint: Pay attension to the type of animal.", str(float((animal1*4)+(animal2 * 2)))],

		[f"Sarah has {quarters} quarters, {dimes} dimes, and {nickels} nickes in her pocket. \n\tIn dollars, how much money does she have? \n\t(DO NOT inlcude the dollar sign in your answer)", str(round((quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05), 2))],

		[f"A square has a side length of {side_length} and there's a circle drawn inside it. \n\tIf the circle meets all of edges of the square, what is the area of the circle?", str(round(((side_length/2)**2) * math.pi, 2))],

		[f"How many degrees is each angle in a shape with {sides} sides?",  str(round(360 / sides, 2))],

		[f"If there is 250ml in one cup, how many ml is there in {cups} cup(s)?", str(float(cups * 250))],

		[f"If an apple has 2.4 grams of fibre, and a pear has 1.25% more grams of fibre, how many grams of fibre are there in {pears} pears?", str(round(2.4 * 1.25 * pears, 0))],

		[f"Kayla is baking cookies. \n\tThe recipe calls for 54g of chocolate chips for every 120g of dough. \n\tIf she has {grams}g of dough, how many grams of chocolate chips does she need to add?", str(round((54/120) * grams, 2))]]

	# Randomly selecting a trivia question and asking player it
	user_question = random.choice(questions)
	print('\n\tQuestion:\n\t', user_question[0])
	answer = input('\n\tAnswer: ')
	
	# Checking if player answered correctly
	# If they did, 100K is added to their account
	# Player 1:
	if config.player == 1:
		config.p1_cards += 1
		if answer == user_question[1]:
			config.player1 += 50
			print('\n\tYou got it right! +$50K\n\tYour account balance is now $' + str(config.player1)+'K.')
		else:
			print('\tThat is incorrect, the correct answer is', user_question[1], 'try again next time!')	

	# Player 2:
	elif config.player == 2:
		config.p2_cards += 1
		if answer == user_question[1]:
			config.player2 += 50
			print('\n\tCorrect! +$50K\n\tYour account balance is now $' + str(config.player2)+'K.')
		else:
			print('\tThat is incorrect, the correct answer is', user_question[1], 'try again next time!')


# Spinner function
def spinner():
	# Imports
	import random
	import config
	
	# Displaying rules
	print('\n\tYou landed on a spinner tile! You will pick 2 numbers, and the other player will pick 1 number.\n\tThen, the spinner will be spun.\n\tIf the spinner lands on one of the selected numbers, that player will win 100K!')

	# Asking player who landed on spinner tile to select 2 numbers
	# Asking other player to select 1 number

	if config.player == 1:
		print('\n\tPlayer 1, pick 2 DIFFERENT numbers between 1 - 10:')
		num1 = int(input('\t\tNumber 1: '))
		num2 = int(input('\t\tNumber 2: '))
	
		print('\n\tPlayer 2, pick 1 number DIFFERENT from the numbers player 1 chose, between 1 - 10:')
		num3 = int(input('\t\tNumber 1: '))
		
		# Spinner
		enter = input('\n\tPress enter to spin the spinner: ')
		number = random.randint(1, 10)
		print('\tThe spinner landed on:', number )
		
		if number == num1 or number == num2:
			print('\tPlayer 1, you won $100K! ')
			config.player1 += 100
			print("\tPlayer 1's account balance now: $" + str(config.player1) + 'k')
		elif number == num3:
			print('\tPlayer 2, you won $100k!')
			config.player2 += 100
			print("\tPlayer 2's account balance now: $" + str(config.player2) + 'k')
		else:
			print('\tNeither player won the $100k.')
			
	elif config.player == 2:
		print('\n\tPlayer 2, pick 2 DIFFERENT numbers between 1 - 10:') 
	
		num1 = int(input('\t\tNumber 1: '))
		num2 = int(input('\t\tNumber 2: '))
		
		print('\n\tPlayer 1, pick 1 number DIFFERENT from the numbers player 1 chose, between 1 - 10:')
		num3 = int(input('\t\tNumber 1: '))
		
		enter = input('\n\tPress enter to spin the spinner: ')
		number = random.randint(1, 10)
		print('\tThe spinner landed on:', number )
		
		if number == num1 or number == num2:
			print('\tPlayer 2, you won $100K! ')
			config.player2 += 100
			print("\tPlayer 2's account balance now: $" + str(config.player2) + 'k')
		elif number == num3:
			print('\tPlayer 1, you won $100k!')
			config.player1 += 100
			print("\tPlayer 1's account balance now: $" + str(config.player1) + 'k')
		else:
			print('\tNeither player won the $100k.')

	return enter