name=input("이름:")

print("-*"*30)
print("\t\t%s's 구구단 PROGRAM 1"%(name))
print("-*"*30)

dan=int(input("단 입력:"))

for i in range(1,10):
    print("%d x %d = %d"%(dan,i,dan*i))
