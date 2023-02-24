a=(int(input("Enter the number : ")))
if a>1: #  direct ah 0 1 vandha thookiru no prime
     for numbers in range(2,a): #2 la irundhu start avu iven soldra number vara 
         if a%numbers==0:
             print("not prime")
             break
         else:
             print ("prime")
             break
else:
    print ("not prime")
#understand concepts;
r=(int(input("Enter the number : ")))
if r%2==0: #remainder = 0 
    print ("yes")
else: 
    print("no")