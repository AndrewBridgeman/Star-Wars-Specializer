# Program to learn how to make checkbox
# and adding callback in kivy

# import kivy module
import kivy

# base Class of your App inherits from the App class.
# app:always refers to the instance of your application
from kivy.app import App

# The :class:`Widget` class is the base class
# required for creating Widgets.
from kivy.uix.widget import Widget

# The Label widget is for rendering text.
from kivy.uix.label import Label

# To use the checkbox must import it from this module
from kivy.uix.checkbox import CheckBox

from kivy.uix.button import Button

# The GridLayout arranges children in a matrix.
# imports the GridLayout class for use in the app.
from kivy.uix.gridlayout import GridLayout

class LabeledChoice:
    def __init__(self, label, layout, initial=True):
        self._label = label
        self._is_active = initial
        check_box = CheckBox(active=initial)
        layout.add_widget(Label(text=label))
        layout.add_widget(check_box)
        check_box.bind(active=self._on_click)

    def _on_click(self, instance, is_active):
        #print(self.label() + str(is_active))
        self._is_active = is_active

    def label(self):
        return self._label

    def is_active(self):
        return self._is_active

class myButton:
    def __init__(self, layout, choices):
        button = Button(text = 'Done', font_size = 30)
        def callback(instance):
            for i in range(len(choices)):
                print(choices[i].label() + ": " + str(choices[i].is_active()))
        button.bind(on_press = callback)
        layout.add_widget(button)


class BunchOfChoices(GridLayout):
    def __init__(self, labels, **kwargs):
        super(BunchOfChoices, self).__init__(**kwargs)
        self.cols = 2
        self._choices = []
        for label in labels:
            widget = LabeledChoice(label, self)
            self._choices.append(widget)
        myButton(self, self._choices)


class Checkboxes:
    def __init__(self, cuts):
        self._cuts = cuts

    def make_window(self):
        window = BunchOfChoices(self._cuts)
        class CheckBoxApp(App):
            def build(self):
                # build is a method of Kivy's App class used
                # to place widgets onto the GUI.
                return window

        if __name__ == '__main__':
            CheckBoxApp().run()


Checkboxes(['1','2','3']).make_window()
