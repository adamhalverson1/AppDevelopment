'''
Version 1.1.2
    Version date: 7/7/2021  
    Removed the StackLayour and ToggleButtons from the paint.kv file. 
    Moved the StackLayout and ToggleButtons to their own file called colorbar.py
        Importing the ColorBar class in main.py. 
                
    
Known Issues: 
    Orange button needs to be corrected
    Buttons are no longer showing on the main app.
        Working on a solution that will allow me to use the colorbar.py file

         
Things to Try:
   I am out of ideas for now. Will keep playing with the classes and functions to see what I can get to work
   
'''

#impoting needed Kivy functions

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout

#importing the ColorBar class created in the colorbar.py file.
from colorbar import ColorBar

#creating the paint widget. This is where the color will be selected 
class PaintWidget(Widget):
    pass

#creating the canvas and allowing it to recieve touch inputs. 
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
   