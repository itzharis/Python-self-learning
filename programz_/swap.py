number1=10
number2=20
print("value of number 1 before swap :",number1)
print("value of number 2 before swap :",number2)
'''
#method `1`
temp=number1
number1=number2
number2=temp
'''
#method2
number1,number2=number2,number1
print (number1,number2)