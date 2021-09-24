'''
Version 1.2.3
    Version date: 7/17/2021  
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
from kivy.uix.layout import Layout
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color, Ellipse, Line

#Creating the Paint Brush widget
class PaintWidget(Widget):
    def paint_color(self):
    #color = ToggleButton()
     #   if self.value:
      #      result.state = 'down'
    
    #Changing the color to Red if the Red Button is selected.
        self.ids.redbtn.text = 'redbtn has been pressed.'
        self.ids.orangebtn.text = 'orangebtn has been pressed.'
        self.ids.yellowbtn.text = 'yellowbtn has been pressed.'
        self.ids.greenbtn.text = 'greenbtn has been pressed.'
        self.ids.bluebtn.text = 'bluebtn has been pressed.'
        self.ids.purplebtn.text = 'purplebtn has been pressed.'
        self.ids.blackbtn.text = 'blackbtn has been pressed.'
        self.ids.whitebtn.text = 'whitebtn has been pressed.'

#Creating the Color Bar to select the colors and the canvas. 
class ColorBar(StackLayout):

    #Telling the app what to do when there is touch input
    def on_touch_down(self, touch):
        paint = PaintWidget()
        paint.center = touch.pos
        self.add_widget(paint)

    #Telling the app what to do when the touch input moves. 
    def on_touch_move(self, touch):
        paint = PaintWidget()
        paint.center = touch.pos
        self.add_widget(paint)
                
#Creating the Paint App
class PaintApp(App):
    pass

#Calling the App 
if __name__ == '__main__':
    PaintApp().run()
   