"""
CP1404 2020 - Practical 7
Student Name: Amy Robinson
Program - Box Layout Demo
"""
from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """BoxLayoutDemo is a Kivy App for box layout demo."""
    def build(self):
        """Build the kivy app from the kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_greet(self):
        """Handle greet message, add input string to output label."""
        # print("test")
        self.root.ids.output_label.text = "Hello " + self.root.ids.input_name.text

    def press_clear(self):
        """Press clear button to reset both the text field and the output label."""
        self.root.ids.output_label.text = "Hello "
        self.root.ids.input_name.text = ''


BoxLayoutDemo().run()
