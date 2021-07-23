import random

num=int(input("lotto 게임수 입력:"))
lotto=[]

for i in range(0,num):
    for j in range(0,6): #리스트에 6번 숫자 추가
        x=random.randrange(1,46)
        lotto.append(x) 
    while(lotto[0]==lotto[1]):
        lotto[1]=random.randrange(1,46)
    while(lotto[0]==lotto[2] or lotto[1]==lotto[2]):
        lotto[2]=random.randrange(1,46)
    while(lotto[0]==lotto[3] or lotto[1]==lotto[3] or lotto[2]==lotto[3]):
        lotto[3]=random.randrange(1,46)
    while(lotto[0]==lotto[4] or lotto[1]==lotto[4] or lotto[2]==lotto[4] or lotto[3]==lotto[4]):
        lotto[4]=random.randrange(1,46)
    while(lotto[0]==lotto[4] or lotto[1]==lotto[4] or lotto[2]==lotto[4] or lotto[3]==lotto[4] or lotto[4]==lotto[5]):
        lotto[5]=random.randrange(1,46)
    
    lotto.sort() #리스트 정렬
    print(lotto)
    lotto.clear() #리스트 초기화