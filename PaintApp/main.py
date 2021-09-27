'''
Version 2.0.3
    Version date: 9/27/2021  
        White Canvas 
        Moved color bar to the top of the window
        Clear button is in the lower left. 
            Struggling with getting this in the appropriate location.
            Clear button is part of a float layout within the Stack layout. 
        Buttons are able to print out a string that is defined in main.py
            Will review how to get the colors associated to this. 
            

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
    
    def on_state(self):
        #Red button functionality
        if self.ids.redbtn.state == "down":
            print('Red button press')
            color = [255, 0, 0, 1]

        #Orange button functionality
        elif self.ids.orangebtn.state =="down":
            print("Orange button press")

        #Yellow button functionality
        elif self.ids.yellowbtn.state =="down":
            print("Yellow button press")

        #Green button functionality 
        elif self.ids.greenbtn.state =="down":
            print("Green button press")

        #Blue button functionality
        elif self.ids.bluebtn.state =="down":
            print("Blue button press")

        #Purple button functionality
        elif self.ids.purplebtn.state =="down":
            print("Purple button press")

        #White button functionality
        elif self.ids.whitebtn.state =="down":
            print("White button press")

        #Black button functionality.
        elif self.ids.blackbtn.state =="down":
            print("Black button press")

        def on_touch_down(self, touch):
            with self.canvas:
                Color(color)
                d = 30.
                Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))

# Create the App class       
class PaintApp(App):
    def build(self):
        return PaintWidget()

#Running the app. 
if __name__ == '__main__':
    PaintApp().run()
   