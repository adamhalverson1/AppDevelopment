from kivy.uix.stacklayout import StackLayout
from kivy.uix.togglebutton import ToggleButton
from kivy.app import App

class ColorBar(App):
#Creating the ColorBar
    def build(self):
        ColorBar = StackLayout(orientation ='lr-bt')
        
        #Adding the color toggle buttons to the color bar
        redbtn = ToggleButton(size_hint= (.125, .2), background_color= [255, 0, 0, 1], group= "Color")
        orangebtn = ToggleButton(size_hint= (.125, .2), background_color= [255, 0, 0, 1], group= "Color")
        yellowbtn = ToggleButton(size_hint= (.125, .2), background_color= [255, 255, 0, 1], group= "Color")
        greenbtn = ToggleButton(size_hint= (.125, .2), background_color= [0, 128, 0, 1], group= "Color")
        bluebtn = ToggleButton(size_hint= (.125, .2), background_color= [0, 0, 255, 1], group= "Color")
        purplebtn = ToggleButton(size_hint= (.125, .2), background_color= [128, 0, 128, 1], group= "Color")
        blackbtn = ToggleButton(size_hint= (.125, .2), background_color= [255, 255, 255, 1], group= "Color")
        whitebtn = ToggleButton(size_hint= (.125, .2), background_color= [0, 0, 0], group= "Color")

        #Adding the colored toggle button widgets 
        ColorBar.add_widget(redbtn)
        ColorBar.add_widget(orangebtn)
        ColorBar.add_widget(yellowbtn)
        ColorBar.add_widget(greenbtn)
        ColorBar.add_widget(bluebtn)
        ColorBar.add_widget(purplebtn)
        ColorBar.add_widget(blackbtn)
        ColorBar.add_widget(whitebtn)

        return ColorBar

        