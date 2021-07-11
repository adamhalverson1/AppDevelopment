'''
Version 1.2.2
    Version date: 7/10/2021  
    Added ID for redbtn in main.py paint.kv. Started the if else statement to choose the color on 
    button click.
    
Known Issues: 
    Orange button needs to be corrected
    Button click does not select the color to be used on the canvas
         
Things to Try:
        In the App class, create a variable for a StackLayout and add each button color with add_widget.
    Reverted to old version to test. 
        Old version had the desired background color and button bar. 
    Trying Toggle button behavior and adding an if else statement to choose the color.
        Each color will be assigned an ID that can be called in the if else statement. 
       
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
    
    def __init__(self, **kwargs):
        super(ColorBar, self).__init__(**kwargs)
        
    def btn_id(self, *args):
        print()     
   
    def on_state(self, widget, value, touch):
        
        if self.ids == 'redbtn' and value == 'down':
            color = (1,0,0)
            with self.canvas:
                Color(*color, mode='hsv')
            d = 10.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))            
        else:
            color = (1,0,0)
            with self.canvas:
                Color(*color, mode='hsv')
            d = 10.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))  

class PaintApp(App):
    pass

if __name__ == '__main__':
    PaintApp().run()
   