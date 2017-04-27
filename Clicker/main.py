from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from kivy.vector import Vector
from kivy.properties import NumericProperty

class CookieButton(ButtonBehavior, Image):
    def __init__(self, **kwargs):
        super(CookieButton, self).__init__(**kwargs)
        self.source = 'cookie.png'
        self.original_size = Vector(self.size)
        self.clicked_size = Vector(self.size) * 1.2

    def on_press(self):
        self.parent.score += 1
        self.size = self.clicked_size
        self.center = self.parent.center

    def on_release(self):
        self.size = self.original_size
        self.center = self.parent.center

class ClickerGame(Widget):
    score = NumericProperty(0)
    pass

class ClickerApp(App):
    def build(self):
        return ClickerGame()


if __name__ == '__main__':
    ClickerApp().run()
