from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

import config
from math import cos, sin, tan, atan


class MoreFunctions(Popup):
    def __init__(self, **kwargs):
        super(MoreFunctions, self).__init__(**kwargs)
        self.title = "More Functions"
        self.title_align = "center"

        self.title_color = [0, 1, 0, 1]
        self.background_color = [0, 0, 0, 1]

        self.content = GridLayout(cols=2)

        for func in config.more_functions:
            self.content.add_widget(Button(text=func, on_press=self.release_function))

        self.content.add_widget(Button(text="Close", on_press=self.dismiss))

    def build(self):
        return self

    def release_function(self, instance):
        config.answer_label.text += instance.text
        self.dismiss()
