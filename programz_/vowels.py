str=input("Enter a string")
vowel="aeiouAEIOU"
print ("input string" ,str)

for i in str:
    if i in vowel:
        str=str.replace(i," ")
print("output string without Vowels",str)
print(i)