'''
Version: 1.0 
Version Date: 9/24/2021

Version Notes:
    Created the calculator GUI. 
    Made functioning numnber buttons.
    Added addition functionality. 

'''
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (500,700)

#Designate .kv file
Builder.load_file('calculator.kv')

class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = '0'

    def button_press(self, button):
        prior = self.ids.calc_input.text

        if prior == "0":
            self.ids.calc_input.text = ''
            self.ids.calc_input.text = f'{button}'
        else:
            self.ids.calc_input.text = f'{prior}{button}'

    def add(self):
        prior = self.ids.calc_input.text
        
        self.ids.calc_input.text = f'{prior}+'

    def subtract(self):
        prior = self.ids.calc_input.text
        
        self.ids.calc_input.text = f'{prior}-'

    def multiply(self):
        prior = self.ids.calc_input.text
        
        self.ids.calc_input.text = f'{prior}*'

    def divide(self):
        prior = self.ids.calc_input.text
        
        self.ids.calc_input.text = f'{prior}/'

    def equals(self):
        prior = self.ids.calc_input.text

        if "+" in prior:
            num_list = prior.split("+")
            answer = 0
            for number in num_list:
                answer = answer + int(number)
            
            self.ids.calc_input.text = str(answer)

        elif "-" in prior:
            num_list = prior.split("-")
            answer = 0
            for number in num_list:
                answer = answer - int(number)
            
            self.ids.calc_input.text = str(answer)

class CalculatorApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    CalculatorApp().run()
