name=input("이름:")

print("-*"*30)
print("\t\t%s의 학점계산 프로그램"%(name))
print("-*"*30)

score=int(input("나의 점수:"))

list=[80,10,30,70,40,50,60,90,20] #리스트선언

list.append(score) #내점수 추가

list.sort()
list.reverse() #역으로 정렬
print(list)

print("%s님의 등수 : %d등" %(name,list.index(score)+1))
