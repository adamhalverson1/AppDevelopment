'''
Version 1.2.1
    Version date: 7/10/2021  
    Reverted to code from version 1.0.1. This version had a white background and ColorBar
               
    
Known Issues: 
    Orange button needs to be corrected
    Buttons are no longer showing on the main app.
        Working on a solution that will allow me to use the colorbar.py file
    

         
Things to Try:
    Create a class for each color in the ColorBar. 
    In the App class, create a variable for a StackLayout and add each button color with add_widget.
    Reverted to old version to test. 
        Old version had the desired background color and button bar. 
       
'''

#impoting needed Kivy functions

from kivy.app import App
from kivy.uix.layout import Layout
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color, Ellipse, Line


class ColorBar(StackLayout):
    
    def on_touch_down(self, touch):
        color = (1, 0, 0)
        with self.canvas:
            Color(*color, mode='hsv')
        d = 30.
        Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
        touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        touch.ud['line'].points += [touch.x, touch.y] 
    
class PaintApp(App):
    pass

if __name__ == '__main__':
    PaintApp().run()
   