name=input("이름 : ")

print("-*"*30)
print("\t\t%s의 시험성적 프로그램"%(name))
print("-*"*30)

subject=input("과목 이름 : ")
score=int(input("점수 : "))

if(score > 90):
    grade="A"
elif(score > 80):
   grade="B"
elif(score > 70):
    grade="C"
else:
    grade="F"

print("%s의 %s과목의 학점 : %c" %(name,subject,grade))

