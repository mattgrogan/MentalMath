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
    
    def generate(self):
        self.problem.generate()
        self.a = str(self.problem.a)
        self.b = str(self.problem.b)
        self.answer = str(self.problem.answer)
        self.operator = self.problem.operator

    def clear(self):
        self.response = ""
        
    def next(self):
        self.clear()
        self.generate()
        
    def correct(self):
        correct_str = "%s %s %s = %s   Good job!" % (self.a, self.operator, self.b, self.answer)
        self.response = correct_str
        
    def on_press(self, button_value):
        self.response = self.response + str(button_value)
        
        def check_answer(*args):
            if self.response == self.answer:
                self.correct()
        
        Clock.schedule_once(check_answer, 1)

class AnswerLabel(Label):
    pass

class MentalMathApp(App):
    
    def build(self):
        
        layout = MentalMathLayout()
        layout.generate()
        return layout
        
if __name__ == '__main__':
    MentalMathApp().run()

