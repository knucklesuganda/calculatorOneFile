from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout

from time import strftime
from math import *


class MainApp(App):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

        self.main_box = BoxLayout(orientation="vertical")
        self.number_grid = GridLayout(cols=3)

        self.operators_grid = BoxLayout(orientation="vertical", size_hint=(0.2, 1))
        self.main_button_box = BoxLayout()
        self.answer_label = Label(color=[0, 1, 0, 1], font_size=50)

        self.more_functions = Popup(title="Functions")
        self.history_popup = Popup(title="History")

    def build(self):
        for i in range(9, -1, -1):
            self.number_grid.add_widget(Button(text=str(i), on_press=self.add_number))

        self.number_grid.add_widget(Button(text=".", on_press=self.add_number))
        self.number_grid.add_widget(Button(text="C", on_press=self.clean_answer))

        self.number_grid.add_widget(Button(text="...", on_press=self.open_functions))
        self.number_grid.add_widget(Button(text="H", on_press=self.open_history))

        for i in ['+', "-", "*", "/", "(", ")"]:
            self.operators_grid.add_widget(Button(text=i, on_press=self.add_number))
        self.operators_grid.add_widget(Button(text="=", on_press=self.get_answer))

        self.main_button_box.add_widget(self.number_grid)
        self.main_button_box.add_widget(self.operators_grid)

        self.main_box.add_widget(self.answer_label)
        self.main_box.add_widget(self.main_button_box)
        return self.main_box

    def clean_answer(self, _):
        self.answer_label.text = ""

    def add_number(self, button):
        self.answer_label.text += button.text

    def get_answer(self, _):
        try:
            self.answer_label.text = str(eval(self.answer_label.text))

            with open("history.txt", "a") as history_file:
                history_file.write(f"{self.answer_label.text}>{strftime('%X')}\n")

        except ZeroDivisionError:
            self.answer_label.text = "Cant divide on zero!"

        except ValueError:
            self.answer_label.text = "Value Error!"

        except Exception as exc:
            self.answer_label.text = str(exc)

    def open_functions(self, _):
        content_grid = GridLayout(cols=2)

        for func in ["cos", "sin", "tan", "sqrt"]:
            content_grid.add_widget(Button(text=func, on_press=self.release_function))
        content_grid.add_widget(Button(text="Close", on_press=self.more_functions.dismiss))

        self.more_functions.content = content_grid
        self.more_functions.open()

    def release_function(self, instance):
        self.answer_label.text += instance.text
        self.more_functions.dismiss()

    def open_history(self, _):
        try:
            history_box = BoxLayout(orientation="vertical")

            with open("history.txt", "r") as history:
                for answer in history.readlines():
                    history_box.add_widget(Button(text=answer, on_press=self.set_answer))

            history_box.add_widget(Button(text="Close", on_press=self.history_popup.dismiss))
            self.history_popup.content = history_box
            self.history_popup.open()
        except:
            self.answer_label.text = "There is no history file!"

    def set_answer(self, new_answer):
        self.answer_label.text = new_answer.text[:new_answer.text.find(">")]
        self.history_popup.dismiss()


if __name__ == '__main__':
    MainApp().run()
