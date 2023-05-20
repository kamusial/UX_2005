import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout

class Touch(Widget):
    btn = ObjectProperty()
    def on_touch_down(self, touch):
        print('Mysz w dole ',touch)
        self.btn.opacity = 0.2
    def on_touch_move(self, touch):
        print('ruch ',touch.spos[0])
    def on_touch_up(self, touch):
        print('Mysz w gorze ',touch.pos)
        self.btn.opacity = 1

class My7App(App):
    def build(self):
        return Touch()

if __name__ == '__main__':
    My7App().run()