
# 1. index / X[i]
class indexer:
    def __getitem__(self, index):
        return index ** 2

# Squarer 클래스의 인스턴스 생성
X = indexer()

for i in range(5):
    print(X[i])

print("\n\n")
# 2. index
class stepper:
    def __getitem__(self, i):
        return self.data[i]

X = stepper()

X.data = "Navy"
for item in X:
    print(item)


# 3. adder / repr
class adder:
    def __init__(self, value=0):
        self.data = value
    def __add__(self,other):
        self.data = self.data + other
    def __repr__(self):
        return self.data
    
X = adder('you')
X + 'tube'
print(X)    