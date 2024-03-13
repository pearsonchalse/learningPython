class wrapper:
    def __init__(self, obj):
        self.wrapped = obj
    def __getattr__(self, attrname):
        print('Trace: ',attrname)
        return getattr(self.wrapped,attrname)
    
""">>> getattr(object, name[, default])
object에 존재하는 속성의 값을 가져온다.

__builtin__ module에 포함된 function 이다. 
출처: https://technote.kr/249 [TechNote.kr:티스토리]
class sample:
    def __init__(self, x):
            self.x = x
c = sample(1)
c.x
"""

x = wrapper([1,2,3])   
x.append(4)
print(x.wrapped)

x = wrapper({"city":"tj", "pop":150})
print(x.keys())
