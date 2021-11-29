'''
Version 2.1.2
    Version date: 9/29/2021  
        Complete rework of python code.
        If else statements did not seem to be the key. 
        Added some new functions that appear to be closer to the desired end result. 
        Updated on_press in paint.kv to use the new function
            root.set_color(self.background_color)
    Corrected button colors.
        Buttons background color now changes when selected, helping identify the current color selected.
            Not the desired shade, all have a blue hint, but it is a step in the right direction.
    Seperated the Canvas and PaintWidgets and ClearButtoninto their own class. 
        This was to make the it so all of the widgets could be present on the screen at the same time.
            They are called in the App portion of main.py 
                Canvas is the main widget. add_widget method is called to add the PaintWidget and ClearButton.

Known Issues: 
    Button click does not select the color to be used on the canvas
        I am now able to click the buttons, before I was only able to paint over them
        The brush color is a black.
            Black is the desired default.
    Buttons are not exlucded from the Canvas and can be colored on.
    Clear button no longer clears since it became its own class.

Things to Try:
       
'''

#impoting needed Kivy functions

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.button import Button
from kivy.graphics import Color, Line
from kivy.core.window import Window

#Creating the paint widget
class PaintWidget(StackLayout):

    #Color picking functionality.
    def red_button(self):
        if self.ids.redbtn == 'down':
            def red(self):
                2.55, .25, .25, 1

    def set_color(self):
        
        orange = self.ids.orangebtn
        yellow = self.ids.yellowbtn
        green = self.ids.greenbtn
        blue = self.ids.bluebtn
        purple = self.ids.purplebtn
        white = self.ids.whitebtn
        black = self.ids.blackbtn


class ClearButton(Widget):
    #Clear button functionality.
    def clear_canvas(self):        
        self.canvas.clear()
        saved = self.children[:]
        self.clear_widgets()        
        for widget in saved:
            self.add_widget(widget)

#clear = ClearButton.clear_canvas

class Canvas(RelativeLayout):
    #Touch input functionality.
    def on_touch_down(self, touch):
    
        if Widget.on_touch_down(self, touch):
            return True

        with self.canvas:
            Color(0, 0, 0, 1)
            Line(circle=(touch.x, touch.y, 2), width=2)
            touch.ud['current_line'] = Line(points=(touch.x, touch.y), width=2)     

    #Touch movement functionality.
    def on_touch_move(self, touch):                               
        if 'current_line' in touch.ud:
            touch.ud['current_line'].points += (touch.x, touch.y)


# Create the App class       
class PaintApp(App):

    def build(self):
        paint_widget = PaintWidget()
        clear_button = ClearButton()
        canvas = Canvas()
        canvas.add_widget(clear_button)
        canvas.add_widget(paint_widget)

        return canvas

#Running the app. 
if __name__ == '__main__':
    PaintApp().run()
   