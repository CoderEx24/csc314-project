from kivy.uix.screenmanager import ScreenManager
from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from kivy.app import App
from loginscreen import *
from signupscreen import *
from os import path

Builder.load_file(path.join(path.dirname(__file__), 'kv', 'main.kv'))

class AppScreen(AnchorLayout):
    pass

class MainApp(App):
    def build(self):
        return AppScreen()
    

if __name__ == '__main__':
    MainApp().run()


