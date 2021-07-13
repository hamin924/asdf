"""a=float(input("첫 번째 인자 :"))
b=float(input("두 번째 인자 :"))

print(a+b) #더하기
print(a-b) #빼기
print(a*b) #곱하기
print(a/b) #나누기

print(a**b) #제곱
print(a%b) #나머지
print(a//b) #몫

aa=input("입력하세요! : ")
print(aa)

a="asdf"
b="10"
c="가나다라마바사\t아자차카타파하"
print(a+b)

a="APPLE          "
print(len(a))
print(a[2])

a="ABCDEFG"
print(a[1:3]) #1에서 3전까지
print(a[1:])
print(a[:4]) #문자열 인덱싱

a="asdf"
print("I ate %c aplles"%(a[0]))

a.count('b')

b="Life is too short!"
b=b.split()
print(b)"""

a=input("이름을 입력하세요:")
print("-*"*30+"*")
print("%s의 계산기 프로그램"%(a))
print("-*"*30+"*")

a=int(input("첫 번째 인자 :"))
b=int(input("두 번째 인자 :"))

print("a+b=%d"%(a+b)) #더하기
print("a-b=%d"%(a-b)) #빼기
print("a*b=%d"%(a*b)) #곱하기
print("a/b=%f"%(a/b)) #나누기

print("제곱:%d"%(a**b)) #제곱
print("나머지:%d"%(a%b)) #나머지
print("몫:%d"%(a//b)) #몫
