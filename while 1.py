name=input("이름 : ")

print("-*"*30)
print("\t\t%s의 반복 계산 프로그램!"%(name))
print("-*"*30)

f=int(input("몇번 반복?"))
num = 1

while(True):
    print("%d번째 반복 중......."%(num))
    a=int(input("첫 번째 인자 :"))
    b=int(input("두 번째 인자 :"))

    print("a+b=%d"%(a+b)) #더하기
    print("a-b=%d"%(a-b)) #빼기
    print("a*b=%d"%(a*b)) #곱하기
    print("a/b=%f"%(a/b)) #나누기

    print("제곱:%d"%(a**b)) #제곱
    print("나머지:%f"%(a%b)) #나머지
    print("몫:%d"%(a//b)) #몫

    print("\n")
    num += 1 #들여쓰기 조심! 

    if(num > f):
        break

    
    

   
