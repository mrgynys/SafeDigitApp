from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from gpt import GPTManager

class APPGUI(BoxLayout):
    data_label = StringProperty("[b][color=84c3be]Цифра:[/color][/b] Чем я могу помочь?\n\n")

    def callback(self):
        if self.ids.Inp.text != "":
            self.set_data_label("[b][color=60cc52]Вы:[/color][/b] " + self.ids.Inp.text + "\n\n")
            self.set_data_label("[b][color=84c3be]Цифра:[/color][/b] " + GPTManager().send(self.ids.Inp.text) + "\n\n")
            self.ids.Inp.text = ""

    def set_data_label(self, data):
        self.data_label += str(data)

class SafeDigit(App):
    def process(self):
        text = self.root.ids.Inp.text

    def build(self):
        return APPGUI()

SafeDigit().run()