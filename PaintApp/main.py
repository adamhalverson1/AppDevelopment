'''
Version 2.0.2
    Version date: 9/27/2021  
    Reverted back to code from version 1.1. This code has a working paint function.
        Color picking needs to be sorted out. 
        Added a clear button.
        Removed button colors for testing
        Removed Kivy version at the top of paint.kv. This corrected the issue with the buttons not resizing when the window siza changed. 

    Working on getting the Buttons to print the button color has been pressed. 
    Once I can figure out that interaction I will hopefully be able to select the paint color using
    the button.
    
    
Known Issues: 
    Button click does not select the color to be used on the canvas
    Button size does not fill the height of the window
    Button sizes are too large, 2 buttons fill the window height. Width is also too large, more than half of the screen is button.
    Buttons are supposed to be at the bottom of the screen going left to right. They are starting at the bottom and going up.
         
Things to Try:
    Trying to print some text with the button clicks. 
       
'''

#impoting needed Kivy functions

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line
from kivy.lang import Builder

class PaintWidget(StackLayout):
   pass

class Canvas(RelativeLayout):
    pass

kv = Builder.load_file("paint.kv")

# Create the App class       
class PaintApp(App):
    def build(self):
        return PaintWidget()


if __name__ == '__main__':
    PaintApp().run()
   