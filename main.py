from kivy.app import App
from kivy.uix.button import Button

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from MoreFunctions import MoreFunctions
from History import History

import config
from math import *


class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

        self.main_box = BoxLayout(orientation="vertical")
        self.number_grid = GridLayout(cols=3)

        self.operators_grid = BoxLayout(orientation="vertical", size_hint=(0.2, 1))
        self.main_button_box = BoxLayout()

        self.history = History()
        self.more_functions = MoreFunctions()

    def build(self):
        for i in range(9, -1, -1):
            self.number_grid.add_widget(Button(text=str(i), on_press=self.add_number))

        self.number_grid.add_widget(Button(text=".", on_press=self.add_number))
        self.number_grid.add_widget(Button(text="C", on_press=self.clean_answer))

        self.number_grid.add_widget(Button(text="F", on_press=self.more_functions.open))
        self.number_grid.add_widget(Button(text="H", on_press=self.history.open))

        for i in config.operations:
            self.operators_grid.add_widget(Button(text=i, on_press=self.add_number))
        self.operators_grid.add_widget(Button(text="=", on_press=self.get_answer))

        self.main_button_box.add_widget(self.number_grid)
        self.main_button_box.add_widget(self.operators_grid)

        self.main_box.add_widget(config.answer_label)
        self.main_box.add_widget(self.main_button_box)
        return self.main_box

    @staticmethod
    def clean_answer(_):
        config.answer_label.text = ""

    @staticmethod
    def add_number(button):
        config.answer_label.text += button.text

    def get_answer(self, _):
        try:
            config.answer_label.text = str(eval(config.answer_label.text))
            self.history.append(config.answer_label.text)

        except ZeroDivisionError:
            config.answer_label.text = "Cant divide on zero!"

        except ValueError:
            config.answer_label.text = "Value Error!"

        except Exception as exc:
            config.answer_label.text = str(exc)


if __name__ == '__main__':
    MainApp().run()
