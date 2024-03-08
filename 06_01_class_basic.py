class FirstClass:
    def setData(self, value):
        self.data = value
    def display(self):
        print("data : ", self.data)
        
#1. multiple instanciation        
x = FirstClass()
y = FirstClass()


x.setData("navy")
y.setData(3.141592)

x.display()
y.display()


#2. inheritance
class SecondClass(FirstClass):
    def display(self):
        print("[SecondClass] Current Value is : %s" % self.data)

z = SecondClass()        
z.setData("real")
z.display()        


#3. operation overloading
class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value
    def __add__(self, other):
        return ThirdClass(self.data + other)
    def __mul__(self, other):
        self.data = self.data * other
        
a = ThirdClass('abc')
a.display()

b = a + 'youtube'
b.display()

a*3
a.display()