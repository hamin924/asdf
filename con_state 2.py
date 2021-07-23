name = input("이름 입력 : ")

print("-*"*30)
print("\t\t%s's 아이스크림 프로그램!"%(name))

nm = [10,10,10,10,10]
print("1. 딸기맛 : 1700원|| %d개\n2. 초코맛 : 2900원||%d개\n3. 바닐라맛 : 3300원||%d개\n4. 메론맛 : 3800원||%d개\n5. 쿠앤크맛 : 4700원||%d개\n"%(nm[0],nm[1],nm[2],nm[3],nm[4]))

print("-*"*30)

n = int(input("주문할 상품의 번호를 입력 : "))
total = int(input("돈을 입력해주세요! : "))
while(True):
    if(n == 1):
        change = total - 1700
        nm[0]-=1
    elif(n == 2):
        change = total - 2900
        nm[1]-=1
    elif(n == 3):
        change = total - 3300
        nm[2]-=1
    elif(n== 4):
        change = total - 3800
        nm[3]-=1
    else:
        change = total - 4700
        nm[4]-=1
    
    print("\n <거스름돈>")

    money=[5000,1000,500,100]
    num=[]

    total = change

    a = change // 5000
    num.append(a)
    change = change % 5000


    a = change // 1000
    num.append(a)
    change = change % 1000


    a = change // 500
    num.append(a)
    change = change % 500


    a = change // 100
    num.append(a)

    for i in range(0,4):
        if(num[i] != 0):
            print("%d원 : %d개"%(money[i],num[i]))

    
    n = int(input("더 주문할 상품의 번호를 입력 : "))

    for i in nm:
        if(i == 0):
            print("재고가 없습니다. 다시입력하세요")




 

