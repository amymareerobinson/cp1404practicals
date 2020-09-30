"""
CP1404 2020 - Practice & Extension
Student Name: Amy Robinson
Program - Greeter Program
"""

from kivy.app import App
from kivy.lang import Builder


class GreeterProgram(App):
    """"""
    def build(self):
        """"""
        self.title = "Greeter Program"
        self.root = Builder.load_file('greeter_program.kv')
        return self.root

    def press_clear(self):
        """"""
        self.root.ids.output_label.text = 'Hello '
        self.root.ids.input_name.text = ''

    def handle_greet(self):
        """"""
        self.root.ids.output_label.text = 'Hello ' + self.root.ids.input_name.text


GreeterProgram().run()
