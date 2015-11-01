from random import randint

class Addition_1x1(object):
    
    def __init__(self):
        self.a = None
        self.b = None
        self.operator = "+"
        self.answer = None
        self.generate()
        
    def generate(self):
        self.a = randint(1, 9)
        self.b = randint(1, 9)
        self.answer = self.a + self.b