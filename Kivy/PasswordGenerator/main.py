'''
Version: 1.0
    Version Date: 12/12/2021

Version Details:
    Initial build of the password generator app 
    

'''
#Importing Kivy modules
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget

#Import additional Python modules 
import random

#importing the kv file. 

Builder.load_file('PasswordGenerator.kv')

#Creating the class for password creation
class PasswordCreation(Widget):
    pass

#Creating the Main App class.
class GeneratorApp(App):
    def build(self):
        return PasswordCreation()

#Runnig the app.
if __name__ == '__main__':
    GeneratorApp().run()