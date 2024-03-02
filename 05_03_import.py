import sys
import os
#현재 폴더의 절대경로를 알아낸 다음 하위폴더(mymodule)을 추가
sys.path.append(os.path.abspath(os.path.dirname(__file__))+"\\mymodule") 

import simple
print("simple.__dict__.keys(): \n", simple.__dict__.keys())
print("simmple.spam: ", simple.spam)

print("set simmple.spam to 2")
simple.spam = 2


import simple #nothing / import : only one / first
print("simmple.spam: ", simple.spam)



print("from small.py")
from small import x,y
print("x,    y : ", x,",       ",y)

print("set x and y[0] to 42")
x = 42
y[0] = 42
print("x,    y : ", x,",       ",y)

print("import small")
import small
print("small.x,    small.y : ", small.x,",       ", small.y) #x : unchanged, y[0] : changed
#'공유된 변경 가능한' 객체는 공유한다.
