from editing import Editing
import os
from kivy.app import App
from os.path import sep, expanduser, dirname
from kivy_garden.filebrowser import FileBrowser
from kivy.utils import platform
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.label import Label

video = Editing('instructions.yaml')


class Choose_Original(App):

    def build(self):
        Window.clearcolor = (0, 0, 0, 0)
        if platform == 'win':
            user_path = dirname(expanduser('~')) + sep + 'Documents'
        else:
            user_path = expanduser('~') + sep + 'Documents'
        browser = FileBrowser(dirselect=True, select_string='Choose Folder', cancel_string='Help',
                              favorites=[(user_path, 'Documents')])
        browser.bind(
            on_success=self._fbrowser_success,
            on_canceled=self._fbrowser_canceled)
        return browser

    def _fbrowser_canceled(self, instance):
        popup = Popup(title='Help',
                      content=Label(text='Please select the file containing\nthe theatrical version of the movie\n'
                                    '(MP4 recommended).'),
                      size_hint=(None, None), size=(600, 600))
        popup.open()

    def _fbrowser_success(self, instance):
        if not instance.selection or '/' not in str(instance.selection):
            popup = Popup(title='Error',
                          content=Label(text='Please select a folder to save to.'),
                          size_hint=(None, None), size=(600, 600))
            popup.open()
        else:
            file = open("original.txt", "w")
            file.write(str(instance.selection))
            file.close()
            App.get_running_app().stop()
            Choose_Special().run()


class Choose_Special(App):

    def build(self):
        Window.clearcolor = (0, 0, 0, 0)
        if platform == 'win':
            user_path = dirname(expanduser('~')) + sep + 'Documents'
        else:
            user_path = expanduser('~') + sep + 'Documents'
        browser = FileBrowser(dirselect=True, select_string='Choose Folder', cancel_string='Help',
                              favorites=[(user_path, 'Documents')])
        browser.bind(
            on_success=self._fbrowser_success,
            on_canceled=self._fbrowser_canceled)
        return browser

    def _fbrowser_canceled(self, instance):
        popup = Popup(title='Help',
                      content=Label(text='Please select the file containing\nthe director\'s cut version of the movie\n'
                                    '(MP4 recommended).'),
                      size_hint=(None, None), size=(600, 600))
        popup.open()

    def _fbrowser_success(self, instance):
        if not instance.selection or '/' not in str(instance.selection):
            popup = Popup(title='Error',
                          content=Label(text='Please select a folder to save to.'),
                          size_hint=(None, None), size=(600, 600))
            popup.open()
        else:
            file = open("special.txt", "w")
            file.write(str(instance.selection))
            file.close()

            if not os.path.isdir('cuts'):
                os.mkdir('cuts')
            original = open("original.txt", "r+")
            original = original.read()
            original = original[2:-2]
            special = open("special.txt", "r+")
            special = special.read()
            special = special[2:-2]
            output_directory = 'cuts'
            try:
                res = video.get_res(original)
                video.cut(original, special, output_directory, res)
            except:
                popup = Popup(title='Error',
                              content=Label(text='Error cutting video file. \nYou may have selected an invalid\nfile '
                                                 'in the previous windows. \nAlso check that the instructions \nin '
                                                 'instructions.yaml are correct.'),
                              size_hint=(None, None), size=(700, 700))
                popup.open()
            else:
                App.get_running_app().stop()


Choose_Original().run()
