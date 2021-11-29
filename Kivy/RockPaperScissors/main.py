'''
Rock Paper Scissors 
    Version: 1.0
    Version Date: 11/29/2021

Version Details:
    This is the initial build of a rock paper scissors game built using python and kivy. 
    The basic template for a Kivy app has been constructed. No functionality has been added at this time.

'''  
#Importing the kv file. 
Builder.load_file('RockPaperScissors.kv')

#Importing the needed functions for Kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

#Creating the class for Rock Paper Scissors. This is left intentionally blank at this time. 
class RockPaperScissors (Widget):
    pass

#Creating the game app class. 
class Game(App):
    def build(self):
        return RockPaperScissors()

#Runnig the app.
if __name__ == '__main__':
    Game().run()


