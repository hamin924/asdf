print("-*"*30)
print("피보나치 수열 프로그램!")
print("-*"*30)



def fib(n):
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    


n = int(input("몇번째까지 출력하시겠습니까?"))

for i in range(1, n + 1):
    print(fib(i))
    

