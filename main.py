from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.properties import StringProperty, ObjectProperty
from problems import TwoDigitAddition

class MentalMathLayout(BoxLayout):
    
    response = StringProperty(None)
    response_label = ObjectProperty(None)
   
    problem = TwoDigitAddition()
    a = StringProperty("")
    b = StringProperty("")
    answer = StringProperty("")
    operator = StringProperty("")
    
    def _generate(self):
        self.problem.generate()
        self.a = str(self.problem.a)
        self.b = str(self.problem.b)
        self.answer = str(self.problem.answer)
        self.operator = self.problem.operator

    def clear(self):
        self.response = ""
        
    def next(self, *args):
        self.clear()
        self._generate()
        
    def enter(self):
        # Check the response
        if self.response == self.answer:
            self.correct()
        else:
            self.incorrect()
        
    def correct(self):
        # Show the response
        correct_str = "Correct! %s %s %s = %s" % (self.a, self.operator, self.b, self.answer)
        self.response = correct_str
        
        Clock.schedule_once(self.next, 1)
        
    def incorrect(self):
        incorrect_str = "%s is incorrect. %s %s %s = %s" % (self.response, self.a, self.operator, self.b, self.answer)
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

