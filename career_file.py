# Career file

# Jobs with a college degree function
def college_pathway():
	# Imports
	import random
	import config

	# Shuffling college cards 
	random.shuffle(config.college_careers)
	end_range = len(config.college_careers) - 1
	print('\n\tEnter 3 different numbers between 0 - ' + str(end_range), 'to draw 3 career cards:')

	# Asking player to randomly pick 3cards
	choice_input = [0] * 3
	for i in range(3):
		choice_input[i] = int(input('\t\t- Number ' + str(i+1) + ': '))
	
	choice = [0] * 3
	for i in range(3):
		choice[i] = config.college_careers[choice_input[i]]

	salary = [0] * 3

	# Matching a salary to the job
	for i in range(3):
		if choice[i] == 'Surgeon':
			salary[i] = 120
		elif choice[i] == 'Engineer':
			salary[i] = 80
		elif choice[i] == 'Lawyer':
			salary[i] = 90
		elif choice[i] == 'Teacher':
			salary[i] = 40
		elif choice[i] == 'Accountant':
			salary[i] = 75
		elif choice[i] == 'Computer Programmer':
			salary[i] = 50
		elif choice[i] == 'Real Estate Agent':
			salary[i] = 100
			
	# Displaying options with salaries
	print('\n\tYour options are:\n\t\t- Option 1: ', choice[0], '~ $' + str(salary[0]) + 'K', '\n\t\t- Option 2: ', choice[1], '~ $' + str(salary[1]) + 'K', '\n\t\t- Option 3: ', choice[2], '~ $' + str(salary[2]) + 'K')
	# Asking player to pick 1 career as their final choice
	option = int(input('\n\tEnter the number of the option you want. Option: '))

	# Player 1: assigning job and salary to their database
	if config.player == 1:
		for i in range(1, 4):
			if option == i:
				config.p1_career = choice[i-1]
				config.p1_salary = salary[i-1]

		# Removing chosen career from career cards deck
		config.college_careers.remove(config.p1_career)

		# Telling player what their job is and removing 100k from account balance
		print('\n\tYour job is now a(n)', config.p1_career, 'with a salary of $' + str(config.p1_salary) + 'K !\n\tYour account balance is now: $', str(config.player1)+ 'K')

	# Same steps = repeated for player 2 if they chose college pathway
	elif config.player == 2:
		for i in range(1, 4):
			if option == i:
				config.p2_career = choice[i-1]
				config.p2_salary = salary[i-1]

		config.college_careers.remove(config.p2_career)

		print('\n\tYour job is now a(n)', config.p2_career, 'with a salary of $' + str(config.p2_salary) + 'K !\n\tYour account balance is now: $', str(config.player2)+ 'K')

	return ''


# Workplace jobs function 
def workplace_pathway():
	import random
	import config

	# Shuffling workplace job cards
	random.shuffle(config.workplace_careers)
	end_range = len(config.workplace_careers) - 1

	# Asking player to randomly pick 3 job cards
	print('\n\tEnter 3 different numbers between 0 - ' + str(end_range), 'to draw 3 career cards')

	# Asking player to randomly pick 3cards
	choice_input = [0] * 3
	for i in range(3):
		choice_input[i] = int(input('\t\t- Number ' + str(i+1) + ': '))
	
	choice = [0] * 3
	for i in range(3):
		choice[i] = config.workplace_careers[choice_input[i]]

	salary = [0] * 3

	for i in range(3):
		# Assigning salaries to the jobs
		#workplace jobs have lower salaries than college career jobs
		if choice[i] == 'Salesperson':
			salary[i] = 25
		elif choice[i] == 'Mechanic':
			salary[i] = 30
		elif choice[i] == 'Athlete':
			salary[i] = 50
		elif choice[i] == 'Hair Stylist':
			salary[i] = 30
		elif choice[i] == 'Police Officer':
			salary[i] = 40
		elif choice[i] == 'Superstar':
			salary[i] = 40
		elif choice[i] == 'Artist':
			salary[i] = 25

	# Displaying options and salaries to player
	print('\n\tYour options are:\n\t\t- Option 1: ', choice[0], '~ $' + str(salary[0]) + 'K', '\n\t\t- Option 2: ', choice[1], '~ $' + str(salary[1]) + 'K', '\n\t\t- Option 3: ', choice[2], '~ $' + str(salary[2]) + 'K')
	option = int(input('\n\tEnter the number of the option you want. Option: '))

	# Player 1: assigning job and salary to their database
	if config.player == 1:
		for i in range(1, 4):
			if option == i:
				config.p1_career = choice[i-1]
				config.p1_salary = salary[i-1]

		# Removing player's job form workplace job card deck
		config.workplace_careers.remove(config.p1_career)
		print('\tYour job is now a(n)', config.p1_career, 'with a salary of $' + str(config.p1_salary) + 'K !')

	# Same steps from above repeated for player 2 if they chose workplace pathway
	elif config.player == 2:
		for i in range(1, 4):
			if option == i:
				config.p2_career = choice[i-1]
				config.p2_salary = salary[i-1]
		
		config.workplace_careers.remove(config.p2_career)
		print('\tYour job is now a(n)', config.p2_career, 'with a salary of $' + str(config.p2_salary), 'K !')

	return ''


# Graduation function
def graduation():
	# Import
	import config
	# Instructions on picking a post-seocndary pathway
	print('\n\tCongratulations, you graduated highschool! Now you will need to pick a post-secondary pathway to follow.')

	print('\tYou will draw 3 career cards randomly and pick a job from your options.')
	print("\n\t\t- College: Pay $100k for a degree & move back 12 spaces to attend school, have a chance to draw a job that pays up to $120k/paycheck.\n\t\t- Workplace: Save money and start working right away, you don't need to pay $100k in student loans.\n\t\t\t\t     However, the highest job you can draw by chance without a degree pays only $50K/paycheck.\n\n\tWhich career path will you follow? (Enter 'Workplace' or 'College')")
	
	career = input('\tCareer pathway: ')
	career = career.capitalize()

	# Assigning pathways to player's database based on their choice
	if config.player == 1:
		if career == 'Workplace':
			config.p1_education = 'Workplace'
			config.p1_spot += 12
		elif career == 'College':
			config.p1_education = 'College'
			config.player1 -= 100

	elif config.player == 2:
		if career == 'Workplace':
			config.p2_education = 'Workplace'
			config.p2_spot += 12
		elif career == 'College':
			config.p2_education = 'College'
			config.player2 -= 100


# Landing a job function:
def job_landing():
	# Imports
	import config

	# Calling specific job functions based on post-secondary pathway chosen
	print('\n\tSTOP: You reached the job tile! Follow the instructions below to get a job!\n\tThe salary is written next to each job.')

	if config.player == 1:
		if config.p1_education == 'College':
			college_output = college_pathway()
			print(college_output)
		elif config.p1_education == 'Workplace':
			workplace_output = workplace_pathway()
			print(workplace_output)
	elif config.player == 2:
		if config.p2_education == 'College':
			college_output = college_pathway()
			print(college_output)
		elif config.p2_education == 'Workplace':
			workplace_output = workplace_pathway()
			print(workplace_output)


# Fired from work function
def fired():
	# Imports
	import config

	college_careers1 = ['Surgeon', 'Engineer', 'Lawyer', 'Teacher', 'Accountant',	'Computer Programmer', 'Real Estate Agent']
	workplace_careers1 = ['Salesperson', 'Mechanic', 'Athlete', 'Hair Stylist', 'Police Officer', 'Superstar', 'Artist']
	print('\n\tOh no! You got fired from your work. You will need to re-apply for a new job. Follow the instructions bellow:')

	# Adding current job back into the card deck
	# Player randomly selects 3 job cards and picks a final card as their new job_landing
	# Player 1:
	if config.player == 1:
		# If college pathway
		if config.p1_career in college_careers1:
			config.college_careers.append(config.p1_career)
			college_output = college_pathway()
			print(college_output)

		# if workplace pathway
		elif config.p1_career in workplace_careers1:
			config.workplace_careers.append(config.p1_career)
			workplace_output = workplace_pathway()
			print(workplace_output)

	# Player 2L
	elif config.player == 2:
		# If college pathway
		if config.p2_career in college_careers1:
			config.college_careers.append(config.p2_career)
			college_output = college_pathway()
			print(college_output)
		# If workplace pathway
		elif config.p2_career in workplace_careers1:
			config.workplace_careers.append(config.p2_career)
			workplace_output = workplace_pathway()
			print(workplace_output)

	return ''


# Payday function
def payday():
	import config
	print('\n\tSTOP: You reached the payday tile!')
	# Updating player's account balance by adding their salary to it

	# Player 1: 
	if config.player == 1:
		config.player1 += config.p1_salary
		print('\n\tAccount: + $' + str(config.p1_salary) + 'K')
		print('\tYour account balance is now: $' + str(config.player1) + 'K')

	# Player 2:
	elif config.player == 2:
		config.player2 += config.p2_salary
		print('\n\tAccount: + $' + str(config.p2_salary) + 'K')
		print('\tYour account balance is now: $' + str(config.player2) + 'K')