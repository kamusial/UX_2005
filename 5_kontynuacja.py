import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty

class MyGrid(Widget):
    imie = ObjectProperty()
    nazw = ObjectProperty()
    wiek = ObjectProperty()

    def btn(self):
        print("Name: ", self.imie.text)
        self.imie.text = ''

class My5App(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    My5App().run()