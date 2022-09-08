'''
This is an app that I am using to test using KivMob and Google AdMob to monetize my applications. 
'''

#Importing the necceissary kivy modules 
from kivy.app import App
from kivy.uix.widget import Widget
from kivmob import KivMob

#Creating the widget class
class myWidget (Widget):
    
    def build(self):
        self.ads = KivMob("ca-app-pub-3345304889044888~1932307468".APP)
        self.ads.new_banner("ca-app-pub-3345304889044888/8991172856".BANNER,False)
        self.ads.request_banner()
        self.ads.show_banner()

#Creating the app class.
class myApp (App):

    def build(self):

        return myWidget()

#Runnig the app.
if __name__ == '__main__':
    myApp().run()
