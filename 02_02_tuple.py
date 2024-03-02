print("  ************* tuple ************* ")

print("\t 1. 순서를 갖는 객체의 집합")
print("\t 2. 오프셋 기반 / 인덱싱")
print("\t 3. 변경불가능")
print("\t 4. 이질적 자료 포함")

tp_empty = ()
print(tp_empty)

tp_onecomp = (0,)
print(tp_onecomp)

tp_embed = ('abc', ('def','gfh'))
print(tp_embed)

tp_concate = tp_onecomp + tp_embed
print(tp_concate)

tp_repeat = tp_onecomp * 3
print(tp_repeat)

print("the purpose of tuple : \n")
print("변경 불가능성을 제공하는 완결성 ... 변경되지 않는다는 것을 확신할 수 있다.")