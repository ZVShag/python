class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Triangle:
    def __init__(self,a,b,c):
        self.A=a
        self.B=b
        self.C=c

    def Perimetr(self):
        self.AB=((self.A.x+self.B.x)**2+(self.A.y+self.B.y)**2)**0.5
        self.BC=((self.B.x+self.C.x)**2+(self.B.y+self.C.y)**2)**0.5
        self.AC=((self.A.x+self.C.x)**2+(self.A.y+self.C.y)**2)**0.5
        return self.AB+self.BC+self.AC
    def Square(self):
        return (self.Perimetr()*(self.Perimetr()-self.AB)(self.Perimetr()-self.BC)(self.Perimetr()-self.AC))**0.5

class Rectangle:
    def __init__(self,a,b,c,d):
        self.A=a
        self.B=b
        self.C=c
        self.D=d
class Square:
    def __init__(self,a,b,c,d):
        self.A=a
        self.B=b
        self.C=c
        self.D=d
class Romb:
    def __init__(self,a,b,c,d):
        self.A=a
        self.B=b
        self.C=c
        self.D=d    
print('Если хочешь создать треугольник нажми 1: \nЕсли хочешь создать прямоугольник нажми 2: \nЕсли хочешь создать квадрат нажми 3:\nЕсли хочешь создать ромб нажми 4:')
f=int(input())
if f==1:
    a=Point(int(input('X= ')),int(input('Y= ')))
    b=Point(int(input('X= ')),int(input('Y= ')))
    c=Point(int(input('X= ')),int(input('Y= ')))
    z=Triangle(a,b,c)
   
    print('Если хочешь найти периметр треугольника нажми 1: \nЕсли хочешь найти площадь треугольника нажми 2: \n')
    r=int(input())
    if r==2:
        print('Сейчас мы расчитаем площадь треугольника')
    if r==3:
        print('Сейчас мы расчитаем площадь квадрата')
