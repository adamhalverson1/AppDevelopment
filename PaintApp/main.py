'''
Version 1.1.0
    Version date: 7/6/2021  
    Trying a different approach with the main.py file and the paint.kv file. 
        Changing the button bar from being a standalone class to making it a child of Paintwidget in main.kv
        Paint brush has been created and is functioning. Color is a set. Working on being able to select with a button bar.         
    
Known Issues: 
    Orange button needs to be corrected
    Button functionality is not currently working.
        Clicking the button does not choose the color, nothing happens. 
        When using the paint brush, the paint covers the buttons. 
         
    
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


    