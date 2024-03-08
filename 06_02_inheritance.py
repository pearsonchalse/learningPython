class Super:
    def method(self):
        print("in Super.method")
        
class Sub(Super):
    def method(self):
        print("Start Sub.method...")
        Super.method(self)
        print("End of Sub.method.")
        
x = Super()
x.method()


print("\n\n")

x = Sub()
x.method()        



