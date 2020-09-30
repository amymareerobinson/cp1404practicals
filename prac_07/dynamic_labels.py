"""
CP1404 2020 - Practical 7
Student Name: Amy Robinson
Program - Dynamic Labels
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabels(App):
    """DynamicLabels is a kivy App for displaying labels."""

    def __init__(self, **kwargs):
        """Construct main app."""
        super().__init__(**kwargs)
        self.names = ["Bob Brown", "Cat Cyan", "Oren Ochre"]

    def build(self):
        """Build the kivy GUI."""
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from list entries add them to the GUI."""
        for name in self.names:
            name_label = Label(text=name)
            self.root.ids.entries_box.add_widget(name_label)


DynamicLabels().run()
