from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from os import path

Builder.load_file(path.join(path.dirname(__file__), 'kv', 'signup.kv'))

class SignupScreen(Screen):
    pass

