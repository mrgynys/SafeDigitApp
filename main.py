import g4f

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

KV = """
MyBL:
        orientation: "vertical"
        size_hint: (0.95, 0.95)
        pos_hint: {"center_x": 0.5, "center_y": 0.5}

        Label:
                font_size: "15sp"
                multiline: True
                text_size: self.width * 0.98, None
                size_hint_x: 1.0
                size_hint_y: None
                height: self.texture_size[1] + 15
                text: root.data_label
        
        TextInput:
                id: Inp
                multiline: False
                padding_y: (5, 5)
                size_hint: (1, 0.5)
                on_text: app.process()

        Button:
                text: "Отправить"
                bold: True
                background_color: '#00FFCE'
                size_hint: (1, 0.5)
                on_press: root.callback()
"""

class MyBL(BoxLayout):
    data_label = StringProperty("Чем я могу помочь?\n")
    
    def callback(self):
        print("Получен запрос: ", self.ids.Inp.text)
        response = g4f.ChatCompletion.create(
            model = "gpt-3.5-turbo",
            messages = [{"role": "user", "content": ("C этого момента пиши только кириллицей. Контекст: " + self.data_label + "\nОтветь на это в контексте: " + self.ids.Inp.text)}],
            stream = True
        )

        for message in response:
            self.set_data_label(message)
        self.set_data_label("\n")
    
    def set_data_label(self, data):
        self.data_label += str(data)


class MyApp(App):
    running = True

    def process(self):
        text = self.root.ids.Inp.text

    def build(self):
        return Builder.load_string(KV)
    
    def on_stop(self):
        self.running = False

MyApp().run()