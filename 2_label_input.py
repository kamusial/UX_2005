import kivy

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button

class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        self.cols = 2

        self.add_widget(Label(text='Imie'))
        self.imie = TextInput(multiline=False)
        self.add_widget(self.imie)

        self.add_widget(Label(text='Nazwisko'))
        self.nazwisko = TextInput(multiline=False)
        self.add_widget(self.nazwisko)

        self.add_widget(Label(text='wiek'))
        self.wiek = TextInput(multiline=False)
        self.add_widget(self.wiek)

        self.add_widget(Button(text='slij', font_size=40))
        self.add_widget(Button(text='slij', font_size=40))

class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()