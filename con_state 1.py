name = input("이름 : ")

print("-*"*30)
print("\t\t%s's 학기 성적 프로그램!"%(name))
print("-*"*30)

subject = ["국어","수학","사회","과학"]

score = []

for i in subject:
    x = int(input("%s 학점 : " %(i)))

    while(x<0 or x>100):

        print("다시 입력하시오")
        x = int(input("%s 학점 : " %(i)) #어려워 다시 공부해ㅠㅠㅠㅠㅠㅠㅠㅠㅠㅠ
        
    score.append(x)

print("\n")

print("<%s님의 이번학기 성적표>"%(name))

grade = []
for i in score:
    if(i >= 90):
        grade.append("A")
    elif(i >= 80):
        grade.append("B")
    elif(i >= 70):
        grade.append("C")
    else:
        grade.append("F")

for i in range(0,4):
      print("%s 과목의 학점 : %s" %(subject[i],grade[i]))   


 
    
    
        
    


    





