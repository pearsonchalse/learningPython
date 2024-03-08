import sys
import os
#현재 폴더의 절대경로를 알아낸 다음 하위폴더(mymodule)을 추가
sys.path.append(os.path.abspath(os.path.dirname(__file__))+"\\mymodule") 

"""
reload는 import/from 과 달리 다음의 특성을 갖는다.
 1. 파이썬의 내장함수이며, 문이 아니다
 2. 이미 존재하는 모듈 객체를 전달하며, 이름을 전달하지는 않는다.
 
예제는 인터프리터를 활용해야 해서 여기서는 넘어가겠다...
"""

