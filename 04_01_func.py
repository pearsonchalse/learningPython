print("********* Function ********* ")

print(" The purpose of using function ")
print("1. reuse")
print("2. discompose the procedure")

print("\n*********  The general format ********* ")
print(" def <name>(arg1, arg2,..., argN):")
print("     <statements>")
print("     return <value>")

print("********* example ********* ")
def intersect(seq1, seq2):
    result = []
    for x in seq1:
        if x in seq2:
            result.append(x)
    return result

youtube = [1,2,3,4,5]
insta = [6,4,2]

print("youtube : ",youtube)
print("insta : ",insta)

answer = intersect(youtube,insta)
print("yoube & insta : ",answer
      )