# Board game functions file


# Introduction function
def intro():

  # Border
  print('-' * 166 + '\n')
  # Center alligning the title
  print('THE GAME OF LIFE'.center(166))
  print()

  # Introduction
  print(
      'Welcome to the game of life! Progress around the board to move forward in life. Get a job, get married, have kids, buy a house….build your dream life! '
      .center(166))
  print(
      'At the end, you and the other player will compare who won at life...literally!'
      .center(166))
  print()
  print(
      'Rules: Each player will take turns rolling the dice and moving forward along the board. You will automatically get stopped at certain sections such as the job'
      .center(166))
  print(
      'and payday tiles, and the ultimale goal is to retire while making the most money.'
      .center(166))
  print()
  print(
      'Tip: For proper format to appear, move the console all the way to the left (hide files display) so that console takes up the entire screen!'
      .center(166))
  print()
  print('Goodluck!'.center(166))

  # Border
  print('\n' + '-' * 166)


# Player 1: game board with integrated functions
def p1_board():
  # Importing functions
  import config
  import random
  from career_file import job_landing
  from career_file import fired
  from career_file import payday
  from family_file import kids_spinner
  from family_file import child
  from family_file import marriage
  from house_file import house
  from retirement_file import retirement
  from others_file import action
  from others_file import trivia
  from others_file import spinner

  # Calculating next spot of player after moving forward
  next_spot = config.p1_spot + config.dice

  # Automatically stopping player if they move past specific tiles on the board
  if config.p1_spot < 20 and next_spot >= 20:
    job_landing()
    config.p1_spot = 20
  elif config.p1_spot < 28 and next_spot >= 28:
    payday()
    config.p1_spot = 28
  elif config.p1_spot < 36 and next_spot >= 36:
    marriage()
    config.p1_spot = 36
  elif config.p1_spot < 43 and next_spot >= 43:
    house()
    config.p1_spot = 43
  elif config.p1_spot < 50 and next_spot >= 50:
    payday()
    config.p1_spot = 50
  elif config.p1_spot < 59 and next_spot >= 59:
    payday()
    config.p1_spot = 59
  elif config.p1_spot < 70 and next_spot >= 60 and next_spot <= 69:
    config.p1_spot = 60

    # Determening next action
    print(
        '\n\tSTOP: You reached the family/house region! Spin to land on a house, child, or just trivia!'
    )

    enter = input('\n\tPress enter to roll the dice: ')
    dice1 = random.randint(1, 5)
    print(enter, '\tYou rolled a:', dice1)
    config.p1_spot += dice1

    if config.p1_spot == 61 or config.p1_spot == 65 or config.p1_spot == 67:
      trivia()
    elif config.p1_spot > 61 and config.p1_spot < 65 or config.p1_spot == 68:
      child()
    elif config.p1_spot == 66 or config.p1_spot == 69:
      house()
    elif config.p1_spot == 70:
      kids_spinner()
  elif config.p1_spot < 70 and next_spot >= 70:
    kids_spinner()
    config.p1_spot = 70
  elif config.p1_spot < 72 and next_spot >= 72:
    payday()
    config.p1_spot = 72
  elif config.p1_spot < 84 and next_spot >= 84:
    payday()
    config.p1_spot = 84
  elif config.p1_spot < 95 and next_spot >= 95:
    payday()
    config.p1_spot = 95
  elif config.p1_spot < 102 and next_spot >= 102:
    payday()
    config.p1_spot = 102
  elif config.p1_spot < 118 and next_spot >= 118:
    payday()
    config.p1_spot = 118
  elif config.p1_spot < 123 and next_spot >= 123:
    retirement()
    config.p1_spot = 123
  # If not automatically stopped, player will follow instructions based on tile they land on
  else:
    config.p1_spot += config.dice
    config.board_1 = config.board_parts[config.p1_spot]

    if config.board_1 == 'Trivia':
      trivia()
    elif config.board_1 == 'Spinner':
      spinner()
    elif config.board_1 == 'Action':
      action()
    elif config.board_1 == 'Fired From Job':
      fired()
    elif config.board_1 == 'Child':
      child()
    elif config.board_1 == 'House':
      house()


# Player 2: game board with integrated functions (same steps from above repeated for player 2)
def p2_board():
  import config
  import random
  from career_file import job_landing
  from career_file import fired
  from career_file import payday
  from family_file import kids_spinner
  from family_file import child
  from family_file import marriage
  from house_file import house
  from retirement_file import retirement
  from others_file import action
  from others_file import trivia
  from others_file import spinner

  next_spot = config.p2_spot + config.dice

  if config.p2_spot < 20 and next_spot >= 20:
    job_landing()
    config.p2_spot = 20
  elif config.p2_spot < 28 and next_spot >= 28:
    payday()
    config.p2_spot = 28
  elif config.p2_spot < 36 and next_spot >= 36:
    marriage()
    config.p2_spot = 36
  elif config.p2_spot < 43 and next_spot >= 43:
    house()
    config.p2_spot = 43
  elif config.p2_spot < 50 and next_spot >= 50:
    payday()
    config.p2_spot = 50
  elif config.p2_spot < 59 and next_spot >= 59:
    payday()
    config.p2_spot = 59
  elif config.p2_spot < 70 and next_spot >= 60 and next_spot <= 69:
    config.p2_spot = 60

    # Determening next action
    print(
        '\n\tSTOP: You reached the family/house region! Spin to land on a house, child, or just trivia!'
    )

    enter = input('\n\tPress enter to roll the dice: ')
    dice1 = random.randint(1, 5)
    print(enter, '\tYou rolled a:', dice1)
    config.p2_spot += dice1

    if config.p2_spot == 61 or config.p2_spot == 65 or config.p2_spot == 67:
      trivia()
    elif config.p2_spot > 61 and config.p2_spot < 65 or config.p2_spot == 68:
      child()
    elif config.p2_spot == 66 or config.p2_spot == 69:
      house()
    elif config.p2_spot == 70:
      kids_spinner()
  elif config.p2_spot < 70 and next_spot >= 70:
    kids_spinner()
    config.p2_spot = 70
  elif config.p2_spot < 72 and next_spot >= 72:
    payday()
    config.p2_spot = 72
  elif config.p2_spot < 84 and next_spot >= 84:
    payday()
    config.p2_spot = 84
  elif config.p2_spot < 95 and next_spot >= 95:
    payday()
    config.p2_spot = 95
  elif config.p2_spot < 102 and next_spot >= 102:
    payday()
    config.p2_spot = 102
  elif config.p2_spot < 118 and next_spot >= 118:
    payday()
    config.p2_spot = 118
  elif config.p2_spot < 123 and next_spot >= 123:
    retirement()
    config.p2_spot = 123
  else:
    config.p2_spot += config.dice
    config.board_2 = config.board_parts[config.p2_spot]

    if config.board_2 == 'Trivia':
      trivia()
    elif config.board_2 == 'Spinner':
      spinner()
    elif config.board_2 == 'Action':
      action()
    elif config.board_2 == 'Fired From Job':
      fired()
    elif config.board_2 == 'Child':
      child()
    elif config.board_2 == 'House':
      house()
