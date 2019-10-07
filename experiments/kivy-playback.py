#!/usr/bin/env pipenv run python

import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.videoplayer import VideoPlayer


kivy.require("1.11.1")


class MyVideoApp(App):
    def build(self):
        self.player = VideoPlayer(
                source='files/A.mp4',
                state='play',
                options={'allow_stretch': True})
        return self.player


MyVideoApp().run()
