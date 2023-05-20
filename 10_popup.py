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
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.popup import Popup

class Widgets(Widget):
    def btn(self):
        show_popup()

class P(FloatLayout):
    pass

class My10App(App):
    def build(self):
        return Widgets()

def show_popup():
    show = P()
    popupWindow = Popup(title="moj popup", content=show, size_hint=(None, None),size=(400,400))
    popupWindow.open()

if __name__ == '__main__':
    My10App().run()