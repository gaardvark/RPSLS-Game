# RPSLS Project (Mini-Project # 1) for Introduction to Interactive Python Programming

import random

def name_to_number(name):
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name == 'scissors':
        return 4
    else:
        print 'This choice is not valid. Please reenter one of the 5 listed choices.'
        
def number_to_name(number):
    if number == 0:
        return'rock'
    elif number == 1:
        return'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return'lizard'
    elif number == 4:
        return'scissors'
    else:
        print 'This number is not valid. Please enter only integers 0-4.'

def rpsls(player_choice):
    print '\n\nPlayer chooses', player_choice
    player_choice = name_to_number(player_choice)
    computer_choice = random.randrange(0, 5)
    print 'Computer chooses', number_to_name(computer_choice)
    outcome = player_choice-computer_choice 
    if outcome < -2 or outcome > 0 < 3:
        print 'Player wins!'
    elif outcome == 0:
        print 'Player and computer tie!'
    else:
        print 'Computer wins!'
        
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric



