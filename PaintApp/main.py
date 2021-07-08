'''
Version 1.1.1
    Version date: 7/7/2021  
    Removed the StackLayour and ToggleButtons from the paint.kv file. 
    Added the StackLayout and ToggleButtons to the main.py file
        Created a seperate class for the ColorBar but that did not work. 
        Added the ColorBar function to the Canvas class, this also did not work. 
        
    
Known Issues: 
    Orange button needs to be corrected
    Buttons are no longer showing on the main app. 
         
Things to Try:
    Play with the classes to see where I can get the ColorBar to show up. 
        Once the color bar is visable I will work on binding the functions for selecting the color. 
    
'''

#impoting needed Kivy functions

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.stacklayout import StackLayout
from kivy.graphics import Color, Ellipse, Line

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

    def ColorBar (StackLayout):
        ColorBar = StackLayout(orientation ='lr-bt')
     
        redbtn = ToggleButton(size_hint= (.125, .2), background_color= [255, 0, 0, 1], group= "Color")
        orangebtn = ToggleButton(size_hint= (.125, .2), background_color= [255, 0, 0, 1], group= "Color")
        yellowbtn = ToggleButton(size_hint= (.125, .2), background_color= [255, 255, 0, 1], group= "Color")
        greenbtn = ToggleButton(size_hint= (.125, .2), background_color= [0, 128, 0, 1], group= "Color")
        bluebtn = ToggleButton(size_hint= (.125, .2), background_color= [0, 0, 255, 1], group= "Color")
        purplebtn = ToggleButton(size_hint= (.125, .2), background_color= [128, 0, 128, 1], group= "Color")
        blackbtn = ToggleButton(size_hint= (.125, .2), background_color= [255, 255, 255, 1], group= "Color")
        whitebtn = ToggleButton(size_hint= (.125, .2), background_color= [0, 0, 0], group= "Color")
    
        ColorBar.add_widget(redbtn)
        ColorBar.add_widget(orangebtn)
        ColorBar.add_widget(yellowbtn)
        ColorBar.add_widget(greenbtn)
        ColorBar.add_widget(bluebtn)
        ColorBar.add_widget(purplebtn)
        ColorBar.add_widget(blackbtn)
        ColorBar.add_widget(whitebtn)
       
        return ColorBar

# Create the App class       
class PaintApp(App):
    def build(self):
        return Canvas()
 

if __name__ == '__main__':
    PaintApp().run()


    