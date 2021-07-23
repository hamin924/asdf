#if elif else

a="apple"
b="banana"
c=1
d=2


if(a=="apple" and b=="lemon"): #조건 만족 안함
    print("fruit")

#while

fruit =1

while(fruit <10):
    print(str(fruit)+"번째 사과 먹기")
    fruit +=1

print("끝")

#for

#list, range

a=[1,2,3,4,5] #리스트 (배열)

for i in a: #a안에 있는 것을 i로 취급
    print(i)


score=[100,90,80,70,60,50]

for s in score:
    if(s == 100):
        print("A")
    elif()