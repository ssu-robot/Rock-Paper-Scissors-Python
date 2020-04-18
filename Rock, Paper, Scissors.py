# Import random module
import random
    
# Creating game rules for user
game_rules = (
    'Welcome to Rock, Paper, Scissors... \n\n'
    'Game rules: \n'
    '1) Rock vs Paper = Paper wins \n'
    '2) Scissors vs Paper = Scissors wins \n'
    '3) Rock vs Scissors = Rock wins \n'
    '4) Rock vs Rock = tie \n6) Paper vs Paper = tie \n7) Scissors vs Scissors = tie \n'
    '8) R = Rock, S = Scissors, P = Paper \n'
    '9) Enter your choice below \n'
      '------------------------------------- \n'
)

print game_rules

# Initial scores
you = 0
computer = 0
draw = 0



while True:
    # Adding options 
    options = ['R', 'P', 'S']
    
    # Getting player input
    player_input = input('\nYour choice: ')
    player_input = player_input.upper()
    
    # Validating user input
    if player_input == 'R' or player_input == 'P' or player_input == 'S':
      
      # Generating random computer input
      print '\nGenerating computer input...'
      computer_input = random.choice(options)

      # Draw
      if player_input == 'R' and computer_input == 'R':
        draw += 1
        print '\n***You = \'R\', Computer = \'R\', Result = Draw***\n'
        
      elif player_input == 'P' and computer_input == 'P':
        draw += 1
        print '\n***You = \'P\', Computer = \'P\', Result = Draw***'
        
      elif player_input == 'S' and computer_input == 'S':
        draw += 1
        print '\n***You = \'S\', Computer = \'S\', Result = Draw***'
      
      # Paper beats Rock
      elif player_input == 'P' and computer_input == 'R':
        you += 1
        print '\n***You = \'P\', Computer = \'R\', Result = Paper wins***'  
        
      elif player_input == 'R' and computer_input == 'P':
        computer += 1
        print '\n***You = \'R\', Computer = \'P\', Result = Paper wins***'  
        
      # Scissors beats Paper
      elif player_input == 'S' and computer_input == 'P':
        you += 1
        print '\n***You = \'S\', Computer = \'P\', Result = Scissors wins***'  
        
      elif player_input == 'P' and computer_input == 'S':
        computer += 1
        print '\n***You = \'P\', Computer = \'S\', Result = Scissors wins***'  
        
      # Rock beats Scissors   
      elif player_input == 'R' and computer_input == 'S':
        you += 1
        print '\n***You = \'R\', Computer = \'S\', Result = Rock wins***'      
      
      elif player_input == 'S' and computer_input == 'R':
        computer += 1
        print '\n***You = \'S\', Computer = \'R\', Result = Rock wins***'   


    # If invalid input entered 
    else:
      print '\n***Invalid input. Please try again***'
      
    # Printing scores
    print '\n***Scores: You = %d, Computer = %d, Draws = %d***' %(you, computer, draw)
    
    # Asking user if they want to keep playing 
    ans = input('\n\nEnter any key to play again or \'N\' to quit: ')
    ans = ans.upper() 
    
    # If user decides to quit  
    if ans == 'N': 
      break
    
# Printing a thank you message at the end of the game
print '\n\n***Final scores: You = %d, Computer = %d, Draws = %d***' %(you, computer, draw)
print("\n***Thanks for playing***") 
    
    
    
    
    
    
    
    
    
    