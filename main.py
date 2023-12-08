import kivy
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import ObjectProperty
import webbrowser


class Container(BoxLayout):

    def parameters(self, value):
        val = self.ids.text_input.text
        if val == "0":
            self.ids.text_input.text = value
        else:
            self.ids.text_input.text = val + value

    def operation(self, operation):
        self.ids.text_input.text = self.ids.text_input.text + operation

    def calculate(self):
        try:
            text_input = eval(self.ids.text_input.text)
            self.ids.text_input.text = str(text_input)
        except:
            self.ids.text_input.text = ('Never gonna give you up!')
            webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')

    def restart(self):
        self.ids.text_input.text = '0'


class MyCalculator(App):
    def build(self):
        return Container()


if __name__ == '__main__':
    MyCalculator().run()
