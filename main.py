from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, ObjectProperty
from kivy.utils import get_color_from_hex
from problems import TwoDigitAddition

class MentalMathLayout(BoxLayout):
    
    response = StringProperty(None)
    response_label = ObjectProperty(None)
    problem = StringProperty(None)
   
    def generate(self):
        pg = TwoDigitAddition()
        self.problem = "%s\n%s %s" % (pg.a, pg.operator, pg.b)
        self.answer = str(pg.answer)

    def clear(self):
        self.response = ""
        
    def next(self, *args):
        self.clear()
        self.generate()
        
    def enter(self):
        # Check the response
        if self.response == self.answer:
            self.correct()
        else:
            self.incorrect()
        
    def correct(self):
        # Show the response
        correct_str = "Correct!"
        self.response = correct_str
        
        Clock.schedule_once(self.next, 1)
        
    def incorrect(self):
        incorrect_str = "Incorrect"
        self.response = incorrect_str
        
        Clock.schedule_once(self.next, 1)
        
    def on_press(self, button_value):
        self.response = self.response + str(button_value)

class ResponseLabel(Label):
    pass

class MentalMathApp(App):
    
    def build(self):
        
        layout = MentalMathLayout()
        layout.next()
        return layout
        
if __name__ == '__main__':
    MentalMathApp().run()

