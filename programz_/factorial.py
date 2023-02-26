factorial=1
num=int(input("enter the value"))

if num<0:
    print("no value for negaive value")
elif num==0:
    print("the factorial of ",num,"is 1")
else:
    for i in range(1,num+1):
        factorial=factorial*i
    print("the factorial of ",num, "is", factorial)


