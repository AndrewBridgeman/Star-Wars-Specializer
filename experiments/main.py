from editing import Editing
from window import Window
from window import MyButton
from kivy.app import App


video = Editing('instructions.yaml')

# video.cut('files/original.mp4', 'files/special2.mp4', 'cuts')]


class CheckBoxApp(App):
    def build(self):
        button = MyButton()
        window = Window(video.get_names(), button.get_button()).make_window()

        def callback(instance):
            choices = window.get_choices()
            video.assemble('cuts', choices, 'final.mp4')

        button.get_button().bind(on_press=callback)

        return window


if __name__ == '__main__':
    CheckBoxApp().run()
