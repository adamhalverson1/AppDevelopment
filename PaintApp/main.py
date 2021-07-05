'''
Version 1.0.1 
    Version date: 7/5/2021
    Initial application build
    Base application opens and looks as expected.
    Orange button needs to be corrected
    Button functionality is not currently working. 
'''

#impoting needed Kivy functions

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.togglebutton import ToggleButton

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