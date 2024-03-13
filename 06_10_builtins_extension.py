class Set:
    def __init__(self, value=[]):
        self.data = []
        self.concat(value)
        
    def concat(self,value):
        for x in value:
            if not x in self.data:
                self.data.append(x)
    
    def intersect(self, other):
        res = []
        for x in self.data:
            if x in other:
                res.append(x)
        return Set(res)
    
    def union(self, other):
        res = self.data[:]
        for x in other:
           if x not in self.data:
               res.append(x)
        return Set(res)
    
    def __len__(self):          # print(len(x))
        return len(self.data)
    def __getitem__(self, key): # print(x[k])
        return self.data[key]
    def __and__(self, other):   # print(x & [1,2,3])
        return self.intersect(other)
    def __or__(self, other):    # print(x | [1,2,3])
        return self.union(other)
    def __repr__(self):         # string 변환
        result = str(self.data)
        return 'set: ' + result
    
myArr = [1,3,5,7]
mySet = Set(myArr)

print('mySet: ', mySet)

print(len(mySet))
print(mySet[0])
print(mySet & [1,2,3])
print(mySet | [1,2,3])
