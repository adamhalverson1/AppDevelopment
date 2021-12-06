'''
Rock Paper Scissors 
    Version: 1.5
    Version Date: 12/6/2021

Version Details:
    This is the initial build of a rock paper scissors game built using python and kivy. 
    The basic template for a Kivy app has been constructed. No functionality has been added at this time.
    Added buttons to the application using the kv file. 
    Added the code for the Rock Paper Scissors game.
    Created a computer variable that randomly selects rock, paper or scissors. 
    Added a slate grey background
    Results are being writted to the GUI by updating the label text. 
    Added labels that display the computer and user choice. 
    Adjust label positions.
    Score is being kept and is displayed in the GUI
    Changed the verbiage for the won and lost messages to include the player and computer choices. 
    Added games play count 
    Added Rock Paper and Scissors images to the buttons
        Removed Rock, Paper and Scissors text from the buttons
    Added spacing in between the buttons. They no longer look like one larger button 
    Adjusted font sizes. 
    Added a reset button that brings all of the values (games played, player and computer scores) back to 0

To Do:
    Make the GUI more appealing. 

Bugs:
    

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

        #If the reset button is selected all values are returned to 0
        if user_choice == "Reset":
            self.ids.games.text = "0"
            self.ids.player.text = "0"
            self.ids.computer.text = "0"   
        
        #Checking to see if the user and computer have the same selection
        elif user_choice == computer:
            self.ids.message.text = "It's a tie game, you and the computer both picked " + user_choice

            #Creating a variable for games played
            games = self.ids.games.text
            #Converting the number of games to an integer
            games = int(games) + 1
            #Converting the number of games back to a string 
            games = str(games)
            #Updating the label with the new player score 
            self.ids.games.text = games            

        
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

            #Creating a variable for games played
            games = self.ids.games.text
            #Converting the number of games to an integer
            games = int(games) + 1
            #Converting the number of games back to a string 
            games = str(games)
            #Updating the label with the new player score 
            self.ids.games.text = games     

            
            
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

            #Creating a variable for games played
            games = self.ids.games.text
            #Converting the number of games to an integer
            games = int(games) + 1
            #Converting the number of games back to a string 
            games = str(games)
            #Updating the label with the new player score 
            self.ids.games.text = games     
            

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


