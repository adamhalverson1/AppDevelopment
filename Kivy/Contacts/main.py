'''
Version 1.0 
    Version Date: 10/15/2021
    Version Details:
        Initial application build 


'''
#importing needed kivy functions 

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

#importing the .kv file. 
Builder.load_file('contacts.kv')

class Contacts (Widget):
    pass

class ContactsApp (App):
    pass

if __name__ == '__main__':
    ContactsApp().run()