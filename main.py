from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty, StringProperty

class MentalMathLayout(BoxLayout):
    
    answer = ObjectProperty(None)
    answer_value = StringProperty(None)

    def clear(self):
        self.answer_value = ""
        
    def on_press(self, button_value):
        self.answer_value = self.answer_value + str(button_value)
        
    
class MentalMathApp(App):
    def build(self):
        layout = MentalMathLayout()
        return layout
        
if __name__ == '__main__':
    MentalMathApp().run()

