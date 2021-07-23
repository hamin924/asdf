num=int(input("몇줄?"))


for i in range(0,num):
    print(" "*(num-(i+1))+"*"*(2*i+1))

for j in range(num-1,0,-1):
    print(" "*((num-1)-(j-1))+"*"*(2*j-1))
