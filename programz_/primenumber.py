a=(int(input("Enter the number : ")))
if a>1:
     for numbers in range(2,a):
         if a%numbers==0:
             print("not prime")
             break
         else:
             print ("prime")
             break
else:
    print ("not prime")