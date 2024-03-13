class Spam:
    def doit(self, message):
        print(message)
        
obj1 = Spam()
x = obj1.doit
x('instance.func -- bound')

t = Spam.doit
t(obj1, 'class.func -- unbound')        