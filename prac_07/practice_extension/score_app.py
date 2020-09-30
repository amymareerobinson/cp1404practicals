"""
CP1404 2020 - Practice & Extension
Student Name: Amy Robinson
Program - Score App
"""
from kivy.app import App
from kivy.lang import Builder


class ScoreApp(App):
    def build(self):
        """"""
        self.title = "Score App"
        self.root = Builder.load_file('score_app.kv')
        return self.root

    def handle_score(self):
        """"""
        if int(self.root.ids.input_name.text) < 50:
            self.root.ids.output_label.text = "Fail"
        else:
            self.root.ids.output_label.text = "Pass"

    def press_clear(self):
        """"""
        self.root.ids.output_label.text = "Score out of 100"
        self.root.ids.input_name.text = ''


ScoreApp().run()
