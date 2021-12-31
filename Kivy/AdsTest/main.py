'''
This is an app that I am using to test using KivMob and Google AdMob to monetize my applications. 
'''

#Importing the necceissary kivy modules 
from kivy.app import App
from kivy.uix.widget import Widget
from kivmob import KivMob

#Creating the widget class
class myWidget (Widget):
    pass

#Creating the app class.
class myApp (App):

    def build(self):
        return myWidget()

#Runnig the app.
if __name__ == '__main__':
    myApp().run()
