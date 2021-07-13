
a=input("이름을 입력하세요:")
print("-*"*30)
print("\t\t%s의 계산기 프로그램"%(a))
print("-*"*30)

a=float(input("첫 번째 인자 :"))
b=float(input("두 번째 인자 :"))

print("a+b=%f"%(a+b)) #더하기
print("a-b=%f"%(a-b)) #빼기
print("a*b=%f"%(a*b)) #곱하기
print("a/b=%f"%(a/b)) #나누기

print("제곱:%f"%(a**b)) #제곱
print("나머지:%f"%(a%b)) #나머지
print("몫:%f"%(a//b)) #몫
