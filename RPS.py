from random import randint
from time import sleep
options = ['R','P','S']
loss_message = 'You lost!'
win_message = 'You won!'
def decide_winner(user_choice, computer_choice):
  print 'You selected: %s' % user_choice
  sleep(1)
  print 'You selected: %s' % computer_choice
  sleep(1)
  user_choice_index = options.index(user_choice)
  computer_choice_index = options.index(computer_choice)
  if user_choice_index == computer_choice_index:
      print 'It is a tie!'
  elif user_choice_index == 0 and computer_choice_index == 2:
      print win_message
  elif user_choice_index == 1 and computer_choice_index == 0:
      print win_message
  elif user_choice_index == 2 and computer_choice_index == 1:
      print win_message
  elif user_choice_index > 2:
      print 'Invalid option was selected'
      return
  else:
      print loss_message

def play_RPS():
  print 'Rock, Paper, or Scissors?'
  user_choice = raw_input('Select R for Rock, p for Paper, or S for Scissors: ')
  sleep(1)
  user_choice = user_choice.upper()
  computer_choice = options[randint(0,len(options)-1)]
  decide_winner(user_choice, computer_choice)
play_RPS() 
  
  