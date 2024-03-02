print("The concept of module loading & namespace & scope")

print("1. module의 statement는 처음 가져올 때 수행")
print("2. 상위수준 assignment는 모듈의 속성 생성")
print("3. module namespacee : __dict__ or dir()")
print("4. module은 단일 scope")

import sys
import os
#현재 폴더의 절대경로를 알아낸 다음 하위폴더(mymodule)을 추가
sys.path.append(os.path.abspath(os.path.dirname(__file__))+"\\mymodule") 
import module2
print("module2.sys: ", module2.sys)
print("module2.name: ", module2.name)
print("module2.__dict__.keys(): \n", module2.__dict__.keys())
print("module2.__name__: ", module2.__name__)
print("module2.__file__: ", module2.__file__)



