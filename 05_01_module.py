print("************ module ************")

print("import : 클라이언트로 모듈 전체를 가져온다.")
print("from : 클라이언트로 모듈 안의 지정된 이름을 가져온다.")
print("reload : 파이썬을 종료하지 않고 모듈 코드를 재적재한다.")

print("The purpose of using module")
print("1. reusing code")
print("2. system namespace division")
print("3. implement shared service or data")


import sys
import os
#현재 폴더의 절대경로를 알아낸 다음 하위폴더(mymodule)을 추가
sys.path.append(os.path.abspath(os.path.dirname(__file__))+"\\mymodule") 
#print(sys.path)

#usage 1
import module1
module1.printer("Hello, import_module")

from module1 import printer
printer("Hello, from_module")
