from editing import Editing
from window import Window
from window import MyButton
from kivy.app import App
from kivy.uix.textinput import TextInput

steps = [0, 0, 1]

video = Editing('instructions.yaml')

if steps[0] == 1:
    main_file = 'files/original.mp4'
    timestamp = '00:00:05.000'
    output_directory = 'files'
    original_name = '1.mp4'
    special_name = '2.mp4'
    video.init_cut(main_file, timestamp, output_directory, original_name, special_name)

if steps[1] == 1:
    original_name = 'files/original.mp4'
    special_name = 'files.special2.mp4'
    output_directory = 'cuts'
    video.cut(original_name, special_name, output_directory)


if steps[2] == 1:
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
