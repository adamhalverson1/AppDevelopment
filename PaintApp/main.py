'''
Version 2.0.2
    Version date: 9/27/2021  
    Reverted back to code from version 1.1. This code has a working paint function.
        Added a clear button.
        Removed button colors for testing
        Removed Kivy version at the top of paint.kv. This corrected the following issues:
            Buttons not resizing when the window size changed.
            Button bar traveling vertically instead of horizontally left to right starting at the bottom as configured. 
            Button size_hint has also been corrected. 
        Moved color bar to the top of the window
        Clear button is in the lower left. 
            Struggling with getting this in the appropriate location.
            Clear button is part of a float layout within the Stack layout. 
                Canvas in Relative layout may need to be primary layout. Will play around and see what happens. 
            

    Working on getting the Buttons to print the button color has been pressed. 
    Working on Canvas color. Default is black, will work with that to try and not over complicate the code for now.
        Desired outcome would be having the option for a white or black canvas. 
    Once I can figure out that interaction I will hopefully be able to select the paint color using
    the button.
    
    
Known Issues: 
    Button click does not select the color to be used on the canvas

Things to Try:

       
'''

#impoting needed Kivy functions

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.lang import Builder

#Creating the paint widget
class PaintWidget(StackLayout):
    pass

#importing the kv file for builder. 
kv = Builder.load_file("paint.kv")

# Create the App class       
class PaintApp(App):
    def build(self):
        return PaintWidget()

#Running the app. 
if __name__ == '__main__':
    PaintApp().run()
   