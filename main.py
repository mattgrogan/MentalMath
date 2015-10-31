from __future__ import division
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.stacklayout import StackLayout
from kivy.properties import StringProperty, ObjectProperty, NumericProperty
from kivy.animation import Animation
from navigationdrawer import NavigationDrawer
from problems import TwoDigitAddition

class MentalMathLayout(BoxLayout):
    
    response = StringProperty(None)
    response_label = ObjectProperty(None)
    problem = StringProperty(None)
    incorrect_label = ObjectProperty(None)
    
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
        self.nbr_correct += 1
        self.update_stats()
        
        Clock.schedule_once(self.next, 0.20)
        
    def incorrect(self):
        self.nbr_incorrect += 1
        self.update_stats()
        
        Clock.schedule_once(self.next, 0.20)
        
    def update_stats(self):
        self.nbr_total = self.nbr_correct + self.nbr_incorrect
        if self.nbr_total > 0:
            self.pct_correct = "{0:.0f}%".format(self.nbr_correct / self.nbr_total * 100)
        else:
            self.pct_correct = "-"
        
    def on_press(self, button_value):
        self.response = self.response + str(button_value)
        
    def reset_score(self):
        self.nbr_correct = 0
        self.nbr_incorrect = 0
        self.update_stats()

class AnimatedLabel(Label):
    
    text = StringProperty(None)
    
    def __init__(self, **kwargs):
        super(AnimatedLabel, self).__init__(**kwargs)
        self.bind(text=self.animate)
    
    def animate(self, *args):

        animation = Animation(opacity = 0.75, duration = 0.10)
        animation += Animation(opacity = 1.00, duration = 0.10)
        animation.start(self.canvas)

class BaseLayout(BoxLayout):
    menu_button = ObjectProperty(None)

class SidePanel(StackLayout):
    reset_score = ObjectProperty(None)

class MentalMathApp(App):
    
    def build(self):
        
        base_layout = BaseLayout()
        
        navigation = NavigationDrawer()
        navigation.anim_type = 'slide_above_simple'
        
        base_layout.menu_button.bind(on_press = lambda j: navigation.toggle_state())
        
        side_panel = SidePanel()
        navigation.add_widget(side_panel)
        
        main_panel = MentalMathLayout()
        main_panel.next()
        side_panel.reset_score.bind(on_press = lambda j: main_panel.reset_score())
        navigation.add_widget(main_panel)
        
        base_layout.add_widget(navigation)
        return base_layout
        
if __name__ == '__main__':
    MentalMathApp().run()

