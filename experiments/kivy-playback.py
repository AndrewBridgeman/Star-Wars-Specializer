#!/usr/bin/env pipenv run python

import kivy
import ffpyplayer
import ffpyplayer.tools
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.videoplayer import VideoPlayer


kivy.require("1.11.1")


class MyVideoApp(App):
    def build(self):
        self.player = VideoPlayer(
                source='out.mp4',
                state='play',
                options={'allow_stretch': True})
        return self.player

print(ffpyplayer.tools.codecs_dec)
MyVideoApp().run()
