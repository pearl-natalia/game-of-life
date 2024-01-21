# Database of player's info file

# Assigning variables as global to be used in other functions
global player1, player2, p1_spot, p2_spot, p1_salary, p2_salary, p1_career, p2_career, college_careers, workplace_careers, players_retired, p1_kids, p2_kids, p1_cards, p2_cards, p1_house, p2_house, p1_house_cost, p2_house_cost, p1_house_red, p2_house_red, p1_house_black, p2_house_black, p1_education, p2_education, board_parts, player, dice, board_1, board_2, house_cards

# Initializing the variables/lists
player = 0
dice = 0

board_1 = ''
board_2 = ''

player1 = 300
player2 = 300

p1_spot = -1
p2_spot = -1

p1_salary = 0
p2_salary = 0

p1_career = ''
p2_career = ''

p1_kids = 0
p2_kids = 0

p1_cards = 0
p2_cards = 0

p1_house = []
p2_house = []
p1_house_cost = []
p2_house_cost = []
p1_house_red = []
p2_house_red = []
p1_house_black = []
p2_house_black = []

p1_education = ''
p2_education = ''

college_careers = ['Surgeon', 'Engineer', 'Lawyer', 'Teacher', 'Accountant', 'Computer Programmer', 'Real Estate Agent']
workplace_careers = ['Salesperson', 'Mechanic', 'Athlete', 'Hair Stylist', 'Police Officer', 'Superstar', 'Artist']

players_retired = []

# House cards
house_cards = ['Houseboat', 'Dream Villa', 'Island Holiday Home', 'Cozy Cottage', 'Family House', 'Studio Apartment', 'Farmhouse', 'Ranch', 'Beach Hut', 'Luxury Apartment', 'Eco House', 'Windmill', 'Teepee', 'City Penthouse']

board_parts = ['*Highschool Graduation*', 'Trivia', 'Trivia', 'Trivia', 'Trivia',	'Trivia', 'Trivia', 'Spinner', 'Trivia', 'Trivia', 'Trivia', 'Trivia', 'Trivia', 'Trivia', 'Action', 'Trivia', 'Trivia', 'Trivia', 'Trivia', 'Trivia', '*Job Landing*', 'Trivia', 'Trivia', 'Trivia', 'Action', 'Trivia', 'Trivia', 'Trivia', '*Payday*', 'Trivia', 'Trivia','Trivia', 'Action', 'Trivia', 'Trivia', 'Trivia', '*Marriage*', 'Spinner', 'Trivia', 'Trivia', 'Trivia','Trivia', 'Trivia', '*Starter House*', 'Trivia', 'Fired from Job', 'Trivia', 'Action', 'Trivia', 'Trivia', '*Payday*','Child', 'Trivia', 'Trivia', 'Spinner', 'Trivia', 'Action', 'Trivia','House', '*Payday*', '*Family & House Region*', 'Trivia', 'Child', 'Child', 'Child', 'Trivia', 'House', 'Trivia', 'Child', 'House', '*Kids Spinner*', 'Trivia', '*Payday*', 'Trivia', 'Spinner', 'Trivia', 'Fired From Job', 'Child', 'Trivia', 'Trivia', 'House', 'Trivia', 'Child', 'Trivia', '*Payday*', 'Trivia', 'Action', 'Trivia', 'Spinner', 'Trivia', 'Fired From Job', 'House', 'Trivia','Trivia', 'Action','*Payday*', 'Trivia','Trivia', 'Spinner', 'Trivia', 'Trivia', 'Child', '*Payday*', 'Trivia', 'Trivia', 'Trivia', 'Trivia', 'Trivia', 'Trivia', 'Trivia', 'Trivia', 'Trivia', 'Trivia', 'Spinner', 'Trivia', 'Trivia', 'Trivia', 'Trivia','*Payday*' 	'Trivia','Trivia',	'Trivia',	'Trivia',	'*RETIRED*']
