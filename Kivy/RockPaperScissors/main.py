'''
Rock Paper Scissors 
    Version: 1.6
    Version Date: 12/12/2021

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
    UI modifications have been made 
        Buttons have been rasied to accomodate a banner add at the bottom of the app
        Size has been changed from root. hieght/width to 800x500px - this will hopefully be better for mobile
    Added code for AdMob using KivMob. 
        Will need to package the app to do further testing.

To Do:
    Add Google AdMob support using KivMob
        Code has been added. Tests do not show ads. Not sure if this is expected or a bug. Need to wait until a production version is ready. 
        Buttons on the buttom of the app have been moved up to support a lower add banner placement. 
            Placement may need to be adjusted more once ads are shown on app.
    All app content is showing in the lower left of the mobile screen. 
        Need to determine why and how to correct.
    

'''  

#Importing KivMob for Google AdMob support 
from io import SEEK_CUR
from kivmob import KivMob

#Importing the Kivy modules for the application.
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label

#importing Random module.
import random

#Importing the kv file. 
Builder.load_file('RockPaperScissors.kv')

#Creating the class for Rock Paper Scissors. This is left intentionally blank at this time. 
class RockPaperScissors (Widget):
        
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

class myAds (Widget):
    def build(self):
        self.ads = KivMob("ca-app-pub-3345304889044888~9817784347".APP)
        self.ads.new_banner("ca-app-pub-3345304889044888/6748235043".BANNER,False)
        self.ads.request_banner()
        self.ads.show_banner()
   
#Creating the game app class. 
class Game(App):

    def build(self):
        ads = myAds()
        rps = RockPaperScissors()

        rps.add_widget(ads)

        return rps

#Runnig the app.
if __name__ == '__main__':
    Game().run()
