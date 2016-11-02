class Dancer(object):
    def dance(self):
        print '"{}" is dancing.....'.format(self.name)

class Student(object):
    def __init__(self, name):
        self.name=name

    def study(self):
        print '"{}" is studying...'.format(self.name)

Student=type('Student', (Dancer,), dict(Student.__dict__))
s1=Student("wind")
s1.dance()