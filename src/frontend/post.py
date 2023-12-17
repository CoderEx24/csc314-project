from kivy.uix.anchorlayout import AnchorLayout
from kivy.lang import Builder
from os import path

Builder.load_file(path.join(path.dirname(__file__), 'kv', 'post.kv'))

class Post(AnchorLayout):
    pass

