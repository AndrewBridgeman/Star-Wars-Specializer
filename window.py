from kivy.uix.label import Label

from kivy.uix.checkbox import CheckBox

from kivy.uix.button import Button

from kivy.uix.gridlayout import GridLayout

from kivy.core.window import Window



class LabeledChoice:
    def __init__(self, label, layout, initial=False):
        self._label = label
        self._is_active = initial
        check_box = CheckBox(active=initial)
        layout.add_widget(Label(text=label , color = [0, 0, 0, 1]))
        layout.add_widget(check_box)
        check_box.bind(active=self._on_click)

    def _on_click(self, instance, is_active):
        self._is_active = is_active

    def label(self):
        return self._label

    def is_active(self):
        return self._is_active


class MyButton:
    def __init__(self, text):
        self._button = Button(text=text, font_size=30)

    def get_button(self):
        return self._button


class BunchOfChoices(GridLayout):
    def __init__(self, labels, button, button2, text, **kwargs):
        super(BunchOfChoices, self).__init__(**kwargs)
        self.cols = 2
        self._choices = []
        for label in labels:
            widget = LabeledChoice(label, self)
            self._choices.append(widget)
        self.add_widget(Label(text="Enter name you wish to call video:", color = [0,0,0,1]))
        self.add_widget(text)
        self.add_widget(button)
        self.add_widget(button2)

    def add_button(self, button):
        self.add_widget(button)

    def get_choices(self):
        results = []
        for i in range(len(self._choices)):
            results.append(self._choices[i].is_active())
        return results


class MyWindow:
    def __init__(self, cuts, button, button2, text):
        self._cuts = cuts
        self._button = button
        self._button2 = button2
        self._text = text

    def make_window(self):
        window = BunchOfChoices(self._cuts, self._button, self._button2, self._text)
        return window
