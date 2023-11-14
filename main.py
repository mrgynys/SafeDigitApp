from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from gpt import GPTManager

class MyLayout(BoxLayout):
    data_label = StringProperty("Чем я могу помочь?\n\n")

    def callback(self):
        self.set_data_label("[i][color=60cc52]Вы:[/color][/i] " + self.ids.Inp.text + "\n")
        self.set_data_label("[i][color=84c3be]Цифра:[/color][/i] " + GPTManager().send(self.ids.Inp.text) + "\n")
        self.ids.Inp.text = ""

    def set_data_label(self, data):
        self.data_label += str(data)

class Mapp(App):
    def process(self):
        text = self.root.ids.Inp.text

    def build(self):
        return MyLayout()

Mapp().run()