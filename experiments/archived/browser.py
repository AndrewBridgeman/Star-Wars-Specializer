from kivy.app import App
from os.path import sep, expanduser, isdir, dirname
from kivy_garden.filebrowser import FileBrowser
from kivy.utils import platform
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.textinput import TextInput
from window import MyButton

# Window.clearcolor = (1, 1, 1, 1)


class CheckBoxApp(App):
    def build(self):
        def on_text(instance, value):
            return value

        text_input = TextInput(text="")
        text_input.bind(text=on_text)

        text_input2 = TextInput(text="")
        text_input2.bind(text=on_text)

        button = MyButton()
        window = Window(names, button.get_button(), text_input, text_input2).make_window()

        def callback(instance):
            print('hi')
            App.get_running_app().stop()
            # choices = window.get_choices()
            # video.assemble('cuts', choices, text_input.text + '/' + text_input2.text + '.mp4')

        button.get_button().bind(on_press=callback)

        return window


class Run:
    def __init__(self, names):
        self._null = 0
        self._names = names

    def run(self):
        CheckBoxApp(self._names).run()
