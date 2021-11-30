import random

def play():
    
    #Getting the users selection
    user = input("Rock, Paper or Scissors\n")
    #changing the users input to uppercse. 
    user = user.upper()
    #Getting the computers choice. Random selection
    computer = random.choice(['ROCK', 'PAPER', 'SCISSORS'])

    #Creating a score variable to user and computer
    userScore = 0
    computerScore = 0

    if user == computer:
        return 'It is a tie game'

    if is_win(user, computer):
        userScore += 1
        return "You Won!"
    
    computerScore +=1
    return "You lost"


def is_win(player, opponent):
    #returns true if the player wins 
    if (player == "ROCK" and opponent == "SCISSORS") or (player == "PAPER" and opponent == "ROCK") or (player == "SCISSORS" and opponent == "PAPER"):
        return True


def gamesPlayed():
    games = 0
    play()
    games += 1


print(gamesPlayed())