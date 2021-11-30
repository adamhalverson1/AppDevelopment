'''
Rock Paper Scissors 
    Version: 1.1
    Version Date: 11/29/2021

Version Details:
    This is the initial build of a rock paper scissors game built using python and kivy. 
    The basic template for a Kivy app has been constructed. No functionality has been added at this time.
    Added buttons to the application using the kv file. 
    Added the code for the Rock Paper Scissors game.

To Do
    Add the functionality to select Rock Paper or Scissors using the buttons.

'''  

#Importing the needed functions for Kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

#importing Random
import random

#Importing the kv file. 
Builder.load_file('RockPaperScissors.kv')

#Creating the class for Rock Paper Scissors. This is left intentionally blank at this time. 
class RockPaperScissors (Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if self.ids.btn == "rock":
            user = 'rock'
        elif self.ids.btn == 'paper':
            user = 'paper'
        elif self.ids.btn == 'scissors':
            user = 'scissors'

    #Creating the function for the Rock Paper Scissors game. 
    def playGame():
        #User selection is based on the selected button
        user = '''Button selection'''
        
        #computer selection is a random selection. 
        computer = computer = random.choice(['ROCK', 'PAPER', 'SCISSORS'])

        #Checking to see if the user and computer have the same selection
        if user == computer:
            return 'It is a tie game'

        if is_win(user, computer):
            return "You Won!"
        
        return "You lost"

def is_win(player, opponent):
    #returns true if the player wins 
    if (player == "ROCK" and opponent == "SCISSORS") or (player == "PAPER" and opponent == "ROCK") or (player == "SCISSORS" and opponent == "PAPER"):
        return True

#Creating the game app class. 
class Game(App):
    def build(self):
        return RockPaperScissors()

#Runnig the app.
if __name__ == '__main__':
    Game().run()


