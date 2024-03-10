class super:
    def hello(self):
        self.data1 = "spam"
        
class sub(super):
    def howdy(self):
        self.data2 = "eggs"


X = sub()
print(X.__dict__)

X.hello()
print(X.__dict__)

X.howdy()
print(X.__dict__)

print("\n\n")
print(super.__dict__)

print(sub.__dict__)

print("\n\n")
X.data3 = "youtube"
print(X.__dict__)