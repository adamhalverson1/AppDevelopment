'''
Rock Paper Scissors 
    Version: 1.4
    Version Date: 12/3/2021

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
    Added a slate grey background
    Results are being writted to the GUI by updating the label text. 
    Added labels that display the computer and user choice. 
    Adjust label positions.
    Score is being kept and is displayed in the GUI
    Changed the verbiage for the won and lost messages to include the player and computer choices. 

To Do
    Make the GUI more appealing. 
    Rock Paper and Scissors icons for the buttons 

'''  

#Importing the needed Kivy modules.
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

#importing Random module.
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
        self.ids.pchoice.text = user_choice

        #Creating the computer selection variable, it will randomly select rock, paper or scissors. 
        computer = random.choice(['Rock', 'Paper', 'Scissors'])
        self.ids.cchoice.text = computer

        #Checking to see if the user and computer have the same selection
        if user_choice == computer:
            self.ids.message.text = "It's a tie game, you and the computer both picked " + user_choice
            
        
        #Checking to see if the user is the winner 
        elif is_win(user_choice, computer):
            self.ids.message.text = "You Won! You picked " + user_choice + " and the computer picked " + computer

            #Creating a variable for the player score
            player_score = self.ids.player.text
            #Converting the score to an integer
            player_score = int(player_score) + 1
            #Converting the player score back to a string 
            player_score = str(player_score)
            #Updating the label with the new player score 
            self.ids.player.text = player_score

            
            
        #Computer won message. 
        else:
            self.ids.message.text = "You lost. You picked " + user_choice + " and the computer picked " + computer

            #Creating a variable for the computer score
            computer_score = self.ids.computer.text
            #Converting the score to an integer
            computer_score = int(computer_score) + 1
            #Converting the player score back to a string 
            computer_score = str(computer_score)
            #Updating the label with the new player score 
            self.ids.computer.text = computer_score
            

#Function for determining the winner
def is_win(player, opponent):
    #returns true if the player wins 
    if (player == "Rock" and opponent == "Scissors") or (player == "Paper" and opponent == "Rock") or (player == "Scissors" and opponent == "Paper"):
        return True

#Creating the game app class. 
class Game(App):

    def build(self):
        return RockPaperScissors()

#Runnig the app.
if __name__ == '__main__':
    Game().run()


