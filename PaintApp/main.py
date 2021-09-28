'''
Version 2.1.0
    Version date: 9/28/2021  
        Complete rework of python code.
        If else statements did not seem to be the key. 
        Added some new functions that appear to be closer to the desired end result. 
        Updated on_press in paint.kv to use the new function
            root.set_color(self.background_color)
        Clear button functionality is now present. 
    
Known Issues: 
    Button click does not select the color to be used on the canvas
        The brush color is a light blue
    Buttons are not exlucded from the Canvas and can be colored on.

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
from kivy.utils import get_color_from_hex


#Creating the paint widget
class PaintWidget(StackLayout):

    #Touch input functionality.
    def on_touch_down(self, touch):
        if Widget.on_touch_down(self, touch):
            return True
        
        with self.canvas:
            Color(*get_color_from_hex('#0080FF80'))
            Line(circle=(touch.x, touch.y, 2), width=2)
            touch.ud['current_line'] = Line(points=(touch.x, touch.y), width=2)     

    #Touch movement functionality.
    def on_touch_move(self, touch):                               
        if 'current_line' in touch.ud:
            touch.ud['current_line'].points += (touch.x, touch.y)

    #Color picking functionality.
    def set_color(self, new_color):
        self.canvas.add(Color(*new_color))    

    #Clear button functionality. 
    def clear_canvas(self):        
        self.canvas.clear()
        saved = self.children[:]
        self.clear_widgets()        
        for widget in saved:
            self.add_widget(widget)


# Create the App class       
class PaintApp(App):
    def build(self):
        self.paint_widget = PaintWidget()
        self.paint_widget.set_color(get_color_from_hex('#2980B9'))
        return self.paint_widget

#Running the app. 
if __name__ == '__main__':
    PaintApp().run()
   