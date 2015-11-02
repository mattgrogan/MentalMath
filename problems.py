from random import randint, choice

def problem_factory(problem_types):
    # TODO: Check if no problem types are selected...
    problem_type = choice(problem_types)[0]
    print problem_type
    
    # Addition
    if problem_type == 'add_1x1':
        return Addition_1x1()
    elif problem_type == 'add_2x2':
        return Addition_2x2()
    elif problem_type == 'add_3x3':
        return Addition_3x3()
    # Subtraction
    elif problem_type == 'subt_1x1':
        return Subtraction_1x1()
    elif problem_type == 'subt_2x2':
        return Subtraction_2x2()
    elif problem_type == 'subt_3x3':
        return Subtraction_3x3()
    else:
        Exception("Unknown problem type")

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
        
class Addition_2x2(object):
    
    def __init__(self):
        self.a = None
        self.b = None
        self.operator = "+"
        self.answer = None
        self.generate()
        
    def generate(self):
        self.a = randint(10, 99)
        self.b = randint(10, 99)
        self.answer = self.a + self.b
        
class Addition_3x3(object):
    
    def __init__(self):
        self.a = None
        self.b = None
        self.operator = "+"
        self.answer = None
        self.generate()
        
    def generate(self):
        self.a = randint(100, 999)
        self.b = randint(100, 999)
        self.answer = self.a + self.b
        
class Subtraction_1x1(object):
    
    def __init__(self):
        self.a = None
        self.b = None
        self.operator = "-"
        self.answer = None
        self.generate()
        
    def generate(self):
        self.a = randint(1, 9)
        self.b = randint(1, 9)
        if self.a < self.b:
            self.a, self.b = self.b, self.a
        self.answer = self.a - self.b
        
class Subtraction_2x2(object):
    
    def __init__(self):
        self.a = None
        self.b = None
        self.operator = "-"
        self.answer = None
        self.generate()
        
    def generate(self):
        self.a = randint(10, 99)
        self.b = randint(10, 99)
        if self.a < self.b:
            self.a, self.b = self.b, self.a
        self.answer = self.a - self.b
        
class Subtraction_3x3(object):
    
    def __init__(self):
        self.a = None
        self.b = None
        self.operator = "-"
        self.answer = None
        self.generate()
        
    def generate(self):
        self.a = randint(100, 999)
        self.b = randint(100, 999)
        if self.a < self.b:
            self.a, self.b = self.b, self.a
        self.answer = self.a - self.b