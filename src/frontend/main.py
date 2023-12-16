from kivy.lang import Builder
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager
from loginscreen import *

Builder.load_file('kv/main.kv')

class MainApp(App):
    def build(self):
        screen_mgr = ScreenManager()
        login_screen = LoginScreen()
        
        screen_mgr.add_widget(login_screen)

        return screen_mgr
    

if __name__ == '__main__':
    MainApp().run()


