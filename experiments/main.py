from editing import Editing
from window import Window
from window import MyButton
from kivy.app import App
from kivy.uix.textinput import TextInput
from  kivy.uix.filechooser import FileChooserListView


video = Editing('instructions.yaml')

# video.cut('files/original.mp4', 'files/special2.mp4', 'cuts')]

filepath = ""




class CheckBoxApp(App):
    def build(self):
        def on_text(instance, value):
            return value

        textinput = TextInput(text="")
        textinput.bind(text=on_text)

        textinput2 = TextInput(text="")
        textinput2.bind(text=on_text)

        button = MyButton()
        window = Window(video.get_names(), button.get_button(), textinput, textinput2).make_window()

        def callback(instance):
            choices = window.get_choices()
            video.assemble('cuts', choices, textinput.text + '/' + textinput2.text + '.mp4')

        button.get_button().bind(on_press=callback)

        return window


if __name__ == '__main__':
    CheckBoxApp().run()
