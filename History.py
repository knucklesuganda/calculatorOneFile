from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
from kivy.uix.button import Button

from time import strftime
import config


class History(Popup):
    def __init__(self, **kwargs):
        super(History, self).__init__(**kwargs)

        self.content = BoxLayout(orientation="vertical", spacing=2)
        self.title_color = [0, 1, 0, 1]

        self.title_align = "center"
        self.background_color = [1, 1, 1, 1]
        self.start()

    @staticmethod
    def append(text):
        with open(config.history_file, "a") as file:
            file.write(f"{text}>{strftime('%X')}\n")

    def start(self):
        try:

            with open(config.history_file, "r") as history:
                for answer in history.readlines():
                    self.content.add_widget(Button(text=answer, on_press=self.set_answer))

            self.content.add_widget(Button(text="Close", on_press=self.dismiss))

        except FileNotFoundError:
            config.answer_label.text = "There is no history file!"

        return self

    def set_answer(self, new_answer):
        config.answer_label.text = new_answer.text[:new_answer.text.find(">")]
        self.dismiss()
