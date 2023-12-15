import kivy
from kivy.app import App
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
import webbrowser

kv = Builder.load_file("CalcAndConvert.kv")


class MainWindow(Screen):

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

    def popup_open(self):
        content = Button(
            text="Закрыть окно",
            size_hint=(None, None),
            size=(170, 50),
            pos_hint=({'x': 0.5, 'y': 0})

        )
        popup = Popup(
            title="О программе",
            content=content,
            size_hint=(None, None),
            size=(200, 200),
            auto_dismiss=False
        )
        popup_text = Label(
            text='Это калькулятор. \nОн служит для работы c\nматемат. операциями \nи числами ',
            size_hint=(None, None),
            size=(800, 600)
            )
        content.add_widget(popup_text)
        content.bind(on_release=popup.dismiss)
        popup.open()


class SecondWindow(Screen):
    days_input = ObjectProperty()

    hours_output = ObjectProperty()
    minutes_output = ObjectProperty()
    seconds_output = ObjectProperty()
    milliseconds_output = ObjectProperty()
    weeks_output = ObjectProperty()

    def convert(self):
        days = int(self.days_input.text)
        hours = days * 24
        minutes = days * 1440
        seconds = minutes * 60
        milliseconds = seconds * 1000
        weeks = days / 7
        self.ids.hours_output.text = str(hours)
        self.ids.minutes_output.text = str(minutes)
        self.ids.seconds_output.text = str(seconds)
        self.ids.milliseconds_output.text = str(milliseconds)
        self.ids.weeks_output.text = str(round(weeks, 2))

    def popup_open_second_window(self):
        content = Button(
            text="Закрыть окно",
            size_hint=(None, None),
            size=(170, 50),
            pos_hint=({'x': 0.5, 'y': 0})

        )
        popup = Popup(
            title="О программе",
            content=content,
            size_hint=(None, None),
            size=(200, 200),
            auto_dismiss=False
        )
        popup_text = Label(
            text='Это конвертер времени. '
                 '\nОн прендназначен для '
                 '\nконвертации дней в '
                 '\nдругие величины',
            size_hint=(None, None),
            size=(800, 600)
            )
        content.add_widget(popup_text)
        content.bind(on_release=popup.dismiss)
        popup.open()


class CalcAndConvert(App):

    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow(name='main'))
        sm.add_widget(SecondWindow(name='second'))
        return sm


if __name__ == '__main__':
    CalcAndConvert().run()
