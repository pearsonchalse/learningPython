class Super:
    def metod(self):
        print("in Super.method")
    def delegate(self):
        print(self.action)

class Inheritor(Super):
    pass

for key in Inheritor.__dict__.keys():
    print(key)
"""
class Replacer(Super):
    def method(self):
        print("in Replacer.method")
        
class Extender(Super):
    def method(self):
        print("Starting Extender.method")
        Super.method(self)
        print("End Extender.method")
        
class Provider(Super):
    def action(self):
        print ("in Provider.action")
        
        
if __name__ == "__main__":
    for cl in (Inheritor, Replacer, Extender):
        print(cl.__name__ + " . . . ")
        cl().method()
        
    
    print("Provider...")
    Provider().delegate()
"""