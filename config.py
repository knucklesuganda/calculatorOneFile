from kivy.uix.label import Label


settings_fields = {
    "Answer label color": "[0, 1, 0, 1]"
}


operations = ['+', "-", "*", "/", "(", ")"]
more_functions = ["cos", "sin", "tan", "atan"]
answer_label = Label(color=settings_fields["Answer label color"], font_size=50)
history_file = "history.txt"