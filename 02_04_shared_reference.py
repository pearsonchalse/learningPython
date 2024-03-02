print(" ************ shared reference ************ ")

print("파이썬에서 레퍼런스(reference)는 객체를 참조하는 변수를 의미합니다.")

list1 = [1,2,3]
list2 = ['a',list1,'b']
dict1 = {'key1':list1, 'key2':2}

print("list1 : ", list1)
print("list2 : ", list2)
print("dict1 : ", dict1)

"""
Three references
list1, list2, dict1
"""
print("\nchange list[1] from 2 to 999\n")
list1[1] = 999

print("list1 : ", list1)
print("list2 : ", list2)
print("dict1 : ", dict1)


print("\nAbout Assignment(치환문)")
print("[case1]")
list1 = [1,2,3]
list3 = ['X',list1,'Y']

print("list3 : ",list3)
list1[1] = 7777777
print("list3 : ",list3)


print("[case2] 한계 슬라이스 사용")
list1 = [1,2,3]
list3 = ['X',list1[:],'Y'] #모든 항목을 추출하여 최상위 수준으로 복사한다.

print("list3 : ",list3)
list1[1] = 7777777
print("list3 : ",list3)