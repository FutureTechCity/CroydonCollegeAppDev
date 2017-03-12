
from kivy.app import App
from kivy.clock import Clock
from kivy.properties import NumericProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.bubble import Bubble
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.widget import Widget

from rock_paper_scissors.main import RPS, Rules, Game


class ScorePanel(FloatLayout):
    score = NumericProperty(0)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        kwargs['spacing'] = 2
        kwargs['pos_hint'] = {'x': 0.5, 'y': 0.1}
        self._hbox = BoxLayout(**kwargs)
        self._label = Label(text='Score:', size_hint=(None, None))
        self._value = Label(text=str(self.score), size_hint=(None, None))
        self.bind(score=self._score_changed)

        self._hbox.add_widget(Widget())
        self._hbox.add_widget(self._label)
        self._hbox.add_widget(self._value)
        self._hbox.add_widget(Widget())
        self.add_widget(self._hbox)

    def _score_changed(self, instance, value):
        self._value.text = str(value)

    def show_text(self, text):
        bubble = Bubble(arrow_pos='top_mid', size_hint=(None, None), size=(200, 100), pos_hint={'x': 0.1, 'y': 0.15})
        bubble.background_color = (1, 0, 0, 0.5)
        bubble.add_widget(Label(text=text))
        self.add_widget(bubble)
        Clock.schedule_once(lambda dt: self.remove_widget(bubble), 1.5)


class ButtonsPanel(BoxLayout):
    def __init__(self, **kwargs):
        self._model = kwargs.pop('model')
        kwargs['orientation'] = 'horizontal'
        super().__init__(**kwargs)

        bg_color = [1, 0.1, 0.1, 0.5]
        self._btn_rock = Button(text='Rock', size_hint=(0.2, 1), background_color=bg_color,
            background_normal="./icons/rock.png"
        )
        self._btn_paper = Button(text='Paper', size_hint=(0.2, 1), background_color=bg_color,
            background_normal="./icons/paper.png",
        )
        self._btn_scissors = Button(text='Scissors', size_hint=(0.2, 1), background_color=bg_color,
            background_normal="./icons/scissors.png",
        )

        self._btn_rock.bind(on_press=self._rock_pressed)
        self._btn_paper.bind(on_press=self._paper_pressed)
        self._btn_scissors.bind(on_press=self._scissors_pressed)

        self.add_widget(self._btn_rock)
        self.add_widget(self._btn_paper)
        self.add_widget(self._btn_scissors)

    def _rock_pressed(self, instance):
        outcome = self._model.play(RPS.rock)
        self.process_result(outcome)

    def _paper_pressed(self, instance):
        outcome = self._model.play(RPS.paper)
        self.process_result(outcome)

    def _scissors_pressed(self, instance):
        outcome = self._model.play(RPS.scissors)
        self.process_result(outcome)

    def process_result(self, outcome):
        self.parent.add_to_score(outcome)


class MainLayout(BoxLayout):
    def __init__(self, **kwargs):
        self._model = kwargs.pop('model')
        kwargs['orientation'] = 'vertical'
        super().__init__(**kwargs)

        self._score_panel = ScorePanel(size=(500, 100), size_hint=(None, None))
        self._buttons_panel = ButtonsPanel(spacing=20, padding=5, model=self._model)
        self.add_widget(self._score_panel)
        self.add_widget(self._buttons_panel)

    def add_to_score(self, outcome):
        self._score_panel.score += outcome.score
        self._score_panel.show_text(outcome.text)


class RockPaperScissorsApp(App):
    def build(self):
        rules = Rules()
        game = Game(rules)
        return MainLayout(model=game)


if __name__ == '__main__':
    RockPaperScissorsApp().run()

