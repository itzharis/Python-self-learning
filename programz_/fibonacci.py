#third numner in series will create sum of first two numbers
n1=0
n2=1
n3=int(input("Enter the value to br displayed by series : "))
#print(n1,n2)
for i in range (0,n3):
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum

print("next one")
for u in range(2,5):
    print(u)
