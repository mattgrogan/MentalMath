from __future__ import division
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from problems import TwoDigitAddition

class MentalMathLayout(BoxLayout):
    
    response = StringProperty(None)
    response_label = ObjectProperty(None)
    problem = StringProperty(None)
    
    nbr_correct = NumericProperty(0)
    nbr_incorrect = NumericProperty(0)
    nbr_total = NumericProperty(0)
    pct_correct = StringProperty("-")
   
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
        self.nbr_correct += 1
        self.update_stats()
        
        Clock.schedule_once(self.next, 1)
        
    def incorrect(self):
        incorrect_str = "Incorrect"
        self.response = incorrect_str
        self.nbr_incorrect += 1
        self.update_stats()
        
        Clock.schedule_once(self.next, 1)
        
    def update_stats(self):
        self.nbr_total = self.nbr_correct + self.nbr_incorrect
        self.pct_correct = "{0:.0f}%".format(self.nbr_correct / self.nbr_total * 100)
        
    def on_press(self, button_value):
        self.response = self.response + str(button_value)

class MentalMathApp(App):
    
    def build(self):
        
        layout = MentalMathLayout()
        layout.next()
        return layout
        
if __name__ == '__main__':
    MentalMathApp().run()

