from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from os import path
from post import *

Builder.load_file(path.join(path.dirname(__file__), 'kv', 'feed.kv'))

class FeedScreen(Screen):
    pass


