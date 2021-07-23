name=input("이름:")

print("-*"*30)
print("\t\t%s의 윤년 계산 프로그램"%(name))
print("-*"*30)


year=int(input("연도 입력 :"))

if(year%4==0 and year%100!=0):
    print("%d는 윤년이다."%(year))
elif(year%400==0):
    print("%d는 윤년이다."%(year))
else:
    print("%d는 윤년이 아니다."%(year))1