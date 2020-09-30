"""
CP1404 2020 - Practical 7
Student Name: Amy Robinson
Program - Convert miles to kilometres
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_TO_KM = 1.60934


class MilesConverterApp(App):
    """MilesConverterApp is a kivy App for converting miles to kilometres."""
    conversion = StringProperty()

    def build(self):
        """Build the kivy app from the kv file."""
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_calculate(self):
        """ handle calculation."""
        value = self.get_miles()
        result = value * MILES_TO_KM
        self.root.ids.output_label.text = str(result)

    def handle_increment(self, increment):
        """Handle increment."""
        miles = self.get_miles() + increment
        self.root.ids.input_miles.text = str(miles)
        self.handle_calculate()

    def get_miles(self):
        """Get miles."""
        try:
            miles = float(self.root.ids.input_miles.text)
            return miles
        except ValueError:
            return 0.0


MilesConverterApp().run()
