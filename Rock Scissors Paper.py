#Rock, scissors and paper
#By:   Silvana Paredes
#Date: 08/08/2025

import random

options = {1: 'Rock', 2: 'Scissors', 3: 'Paper'}

#Enter your option
while True:
  user = input('Enter your option: 1 = rock, 2 = scissors or 3 = paper: \n')
  if user.isdigit():
    user_num = int(user)
    if user_num in options:
      break
    else:
      print('Enter a number between 1 and 3')

#Get user description
user_text = options[user_num]
          
#Get a random option
roll = random.randint(1,3)

#Get computer description
roll_text = options[roll]

#Evaluate your option
if user_num == roll:
  print('Tie. Both chose', roll_text)
elif ( user_num == 1 and roll == 2 ) or \
     ( user_num == 2 and roll == 3 ) or \
     ( user_num == 3 and roll == 1 ):
  print('You won. You chose', user_text, ' and the computer chose', roll_text)
elif ( user_num == 1 and roll == 3 ) or \
     ( user_num == 2 and roll == 1 ) or \
     ( user_num == 3 and roll == 2 ):
  print('The computer won. You chose', user_text, ' and the computer chose', roll_text)

print('Thank you!')

  
  
