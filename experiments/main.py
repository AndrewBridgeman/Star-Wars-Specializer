from editing import Editing
from window import Window
from window import MyButton
from kivy.app import App
from kivy.uix.textinput import TextInput


video = Editing('instructions.yaml')

# video.cut('files/original.mp4', 'files/special2.mp4', 'cuts')


class CheckBoxApp(App):
    def build(self):
        def on_text(instance, value):
            return value

        text_input = TextInput(text="")
        text_input.bind(text=on_text)

        text_input2 = TextInput(text="")
        text_input2.bind(text=on_text)

        button = MyButton()
        window = Window(video.get_names(), button.get_button(), text_input, text_input2).make_window()

        def callback(instance):
            choices = window.get_choices()
            video.assemble('cuts', choices, text_input.text + '/' + text_input2.text + '.mp4')

        button.get_button().bind(on_press=callback)

        return window


if __name__ == '__main__':
    CheckBoxApp().run()
