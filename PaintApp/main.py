'''
Version 2.0
    Version date: 9/24/2021  
    Reverted back to code from version 1.1. This code has a working paint function.
        Color picking needs to be sorted out. 
    Working on getting the Buttons to print the button color has been pressed. 
    Once I can figure out that interaction I will hopefully be able to select the paint color using
    the button.
    
    
Known Issues: 
    Orange button needs to be corrected
    Button click does not select the color to be used on the canvas
         
Things to Try:
    Trying to print some text with the button clicks. 
       
'''

#impoting needed Kivy functions

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout

class PaintWidget(Widget):
    pass

class Canvas(RelativeLayout):

    def on_touch_down(self, touch):
        paint = PaintWidget()
        paint.center = touch.pos
        self.add_widget(paint)

    def on_touch_move(self, touch):
        paint = PaintWidget()
        paint.center = touch.pos
        self.add_widget(paint)

# Create the App class       
class PaintApp(App):
    def build(self):
        return Canvas()


if __name__ == '__main__':
    PaintApp().run()
   