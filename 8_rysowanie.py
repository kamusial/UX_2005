import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Rectangle
from kivy.graphics import Color
from kivy.graphics import Line
class Touch(Widget):
    def __init__(self, **kwargs):
        super(Touch, self).__init__(**kwargs)

        with self.canvas:
            Color(1, 0, 0, 0.5, mode='rgba')
            self.rect1 = Rectangle(pos=(0,0), size=(50,60))
            Color(0, 1, 0, 0.5, mode='rgba')
            self.rect2 = Rectangle(pos=(40,270), size=(30,160))
            Color(0, 0, 1, 0.5, mode='rgba')
            self.rect3 = Rectangle(pos=(400, 300), size=(150,60))
            Color(1, 0, 1, 1, mode='rgba')
            Line(points=(20,30,400,40,50,450,750,540,30,20))


    btn = ObjectProperty()
    def on_touch_down(self, touch):
        print('Mysz w dole ',touch)
        self.btn.opacity = 0.2
        self.rect1.pos = touch.pos
        self.btn.pos[1] = touch.pos[1]
        self.btn.size[0] += 10
    def on_touch_move(self, touch):
        print('ruch ',touch.spos[0])
        self.rect2.pos = touch.pos
    def on_touch_up(self, touch):
        print('Mysz w gorze ',touch.pos)
        self.btn.opacity = 1

class My7App(App):
    def build(self):
        return Touch()

if __name__ == '__main__':
    My7App().run()