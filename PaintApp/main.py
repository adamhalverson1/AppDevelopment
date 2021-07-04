from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color, Ellipse, Line
from kivy.uix.togglebutton import ToggleButton


class ColorBar(StackLayout):

    def Red_Button(self, touch):
        with self.canvas:
            Color(1, 0, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def Orange_Button(self,touch):
        with self.canvas:
            Color(1, 0, 0)
            d = 30.
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            touch.ud['line'] = Line(points=(touch.x, touch.y))
        
    def Yellow_Button(self):
        Color(1, 1, 0)

    def Green_Button(self):
        Color(1, 0, 0)

    def Blue_Button(self):
        Color(1, 0, 0)

    def Purple_Button(self):
        Color(1, 0, 0)

    def Black_Button(self):
        Color(1, 0, 0)

    def White_Button(self):
        Color(1, 0, 0)




class PaintApp(App):
    pass
'''    def build(self):
        parent = Widget()
        self.painter = PaintWidget()
        clearbtn = Button(text='Clear')
        clearbtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        return parent
    
    def clear_canvas(self, obj):
        self.painter.canvas.clear()

'''

if __name__ == '__main__':
    PaintApp().run()