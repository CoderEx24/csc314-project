from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from os import path

Builder.load_file(path.join(path.dirname(__file__), 'kv', 'login.kv'))

class LoginScreen(Screen):
    pass

