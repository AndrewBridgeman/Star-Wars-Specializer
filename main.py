from editing import Editing
from window import MyWindow
from window import MyButton
from kivy.app import App
from kivy.uix.textinput import TextInput
from os.path import sep, expanduser, dirname
from kivy_garden.filebrowser import FileBrowser
from kivy.utils import platform
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label

step = 2

video = Editing('instructions.yaml')

# File cutting
if step == 1:
    # change these two lines
    original_path = 'versions/original.mp4'
    special_path = 'versions/special.mp4'
    ########################
    output_directory = 'cuts'
    res = video.get_res(original_path)
    video.cut(original_path, special_path, output_directory, res)

# File assembly
if step == 2:
    class Choose_FolderApp(App):

        def build(self):
            Window.clearcolor = (0, 0, 0, 0)
            if platform == 'win':
                user_path = dirname(expanduser('~')) + sep + 'Documents'
            else:
                user_path = expanduser('~') + sep + 'Documents'
            browser = FileBrowser(dirselect=True, select_string='Choose Folder', cancel_string='',
                                  favorites=[(user_path, 'Documents')])
            browser.bind(
                        on_success=self._fbrowser_success,
                        on_canceled=self._fbrowser_canceled)
            return browser

        def _fbrowser_canceled(self, instance):
            x = 1

        def _fbrowser_success(self, instance):
            if not instance.selection or '/' not in str(instance.selection):
                popup = Popup(title='Error',
                              content=Label(text='Please select a folder to save to'),
                              size_hint=(None, None), size=(600, 600))
                popup.open()
            else:
                file = open("filepath.txt", "w")
                file.write(str(instance.selection))
                file.close()
                App.get_running_app().stop()
                AssembleApp().run()


    class AssembleApp(App):
        def build(self):
            Window.clearcolor = (1, 1, 1, 1)

            def on_text(instance, value):
                return value

            text_input = TextInput(text="")
            text_input.bind(text=on_text)

            button = MyButton("Assemble")
            button2 = MyButton("Go back")
            window = MyWindow(video.get_names(), button.get_button(), button2.get_button(), text_input).make_window()

            def callback(instance):
                choices = window.get_choices()
                file = open("filepath.txt", "r+")
                path = file.read()
                path = path[2:-2]
                if not text_input.text:
                    popup = Popup(title='Error',
                                  content=Label(text='Please enter a name for your video'),
                                  size_hint=(None, None), size=(600, 600))
                    popup.open()
                elif '.mp4' in text_input.text:
                    popup = Popup(title='Error',
                                  content=Label(text='Please do not include \'.mp4\' in your video name'),
                                  size_hint=(None, None), size=(700, 700))
                    popup.open()
                else:
                    try:
                        video.assemble('cuts', choices, path + '/' + text_input.text + '.mp4')
                    except:
                        popup = Popup(title='Error',
                                      content=Label(text='Error creating video file. \nYou may have selected a file '
                                                         'instead \nof a folder in the previous window. \nAlso make '
                                                         'sure that your files are in \nthe \'cuts\' folder.'),
                                      size_hint=(None, None), size=(700, 700))
                        popup.open()

                    else:
                        App.get_running_app().stop()

            def callback2(instance):
                App.get_running_app().stop()
                Choose_FolderApp().run()

            button.get_button().bind(on_press=callback)
            button2.get_button().bind(on_press=callback2)

            return window

    Choose_FolderApp().run()
