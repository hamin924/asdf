"""list1 = [1,3,5,6,85,45]
list2 = ["apple", "banana", "lemon"]
list3 = [1,2,3,4,5,6,7,8,9,10]
list4 = [4,5,6]

list2[1] = "melon"

print(list2)
print(list1)
print(list2[1])
print(list3[-1]) #뒤에서는 -1부터 셈

print(list1 + list4)
print(len(list1))

del list2[0]
print(list2)

list1.sort()
print(list1)
list1.reverse()
print(list1)
print(list1.index(45))

print(list1.count(1))
"""


#if elif else

"""fruit = 0

if(fruit == 0):
    print("과일 못 먹음")
else:
    print("과일 먹기")

score = 70

if(score == 100):
    print("A+")
elif (score > 70):
    print("B+")
elif(score >50):
    print("C+")
else:
    print("F")"""

fruit = ["apple","banana","melon"]

if("apple" in fruit): #사과가 과일 안에 있으면
    print("사과 있음")
else:
    print("사과 없음")