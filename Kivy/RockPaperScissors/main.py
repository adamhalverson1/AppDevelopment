'''
Rock Paper Scissors 
    Version: 1.2
    Version Date: 12/1/2021

Version Details:
    This is the initial build of a rock paper scissors game built using python and kivy. 
    The basic template for a Kivy app has been constructed. No functionality has been added at this time.
    Added buttons to the application using the kv file. 
    Added the code for the Rock Paper Scissors game.
    Created functions that will print rock, paper and scissors to the console when pressed.
        I should be able to use this function to pass the selection to the user variable.
    Created a computer variable that randomly selects rock, paper or scissors. 
    Coded the rock paper scissors game. Results are printed to the console. 
        This is fully functional. 

        

To Do
    Write the results to the GUI
    Keep count of the score and write that to the GUI. 
    Make the GUI more appealing. 

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

    #Function for running the rock paper scissors game using player selection by button and random computer selection.
    def button_press (self, user_choice):
        self.user_choice = user_choice
        print(user_choice)

        #Creating the computer selection variable, it will randomly select rock, paper or scissors. 
        computer = random.choice(['ROCK', 'PAPER', 'SCISSORS'])
        print(computer)

        #Checking to see if the user and computer have the same selection
        if user_choice == computer:
            print ("It is a tie game")
        
        #Checking to see if the user is the winner 
        elif is_win(user_choice, computer):
            print("You Won!")
        #Computer won message. 
        else:
            print("You Lost")

#Function for determining the winner
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


