from random import randint

class TwoDigitAddition(object):
    
    def __init__(self):
        self.a = None
        self.b = None
        self.operator = "+"
        self.answer = None
        self.generate()
        
    def generate(self):
        self.a = randint(10, 20)
        self.b = randint(10, 20)
        self.answer = self.a + self.b