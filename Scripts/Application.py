import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder
from GestureToSpeech import *
from SpeechToGesture import *


Builder.load_file('Design.kv')


class MyLayout(Widget):

    def GTS_App(self):
        GTS()

    def STG_App(self):
        STG()


class MyApp(App):
    def build(self):
        return MyLayout()


if __name__ == '__main__':
    MyApp().run()
