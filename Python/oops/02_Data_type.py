class Fraction:
    #parameterized constructor
    def __init__(self,x,y):
        self.num = x
        self.den = y

    def __str__(self):
        return '{}/{}'.format(self.num,self.den)
    
    def __add__(self,other):
        new_num = (self.num * other.den) + (self.den * other.num)
        new_den = (self.den * other.den)
        return '{}/{}'.format(new_num,new_den)
    

fr1 = Fraction(3,4)
fr2 = Fraction(5,10)
print(fr1)
print(fr2)
print(fr1 + fr2) 