import random
base=[0,0,0]


for i in range(0,3):
    base[i]=random.randrange(0,10)

    
print(base)   

num=9

while(num>0):
    
    n=int(input("세자리 수를 입력:"))

    a=n//100
    n=n%100
    b=n//10
    c=n%10
    

    if(a==b or a==c or b==c):
        print("중복된 숫자입니다. 다시 입력하세요")
        n=int(input("세자리 수를 입력:"))


    ball=0
    strike=0

    if(a==base[0] and b==base[1] and c==base[2]):
        print("success!")
        break

    if(a==base[0]):
        strike+=1
    elif(a==base[1] or a==base[2]):
        ball+=1
    

    if(b==base[1]):
        strike+=1
    elif(b==base[0] or b==base[2]):
        ball+=1
    
    

    if(c==base[2]):
        strike+=1
    elif(c==base[0] or c==base[1]):
        ball+=1
    
    

    
    if(a!=base and b!=base and c!=base):
        print("out!")
    else:
        print("strike: %d, ball: %d"%(strike,ball))
    
    num-=1
    print("%d번 기회가 남았습니다" %(num))
    
