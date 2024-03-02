print("  ************* file ************* ")

print("\t file이란 운영체제에서 관리되는 자료를 저장하는 방(이름을 가짐)")
print("\t 내장된 객체 자료형")
print("\t open : 파일 객체 생생하고 시스템에 존재하는 파일에 링크한다.")
print("\t open함수 호출 후 :파일 객체 메소드 호출 --> 외부 파일을 read/write")

myfile = open('01_01_print.py','r')
str = myfile.readline()
print(str)

myfile.close()