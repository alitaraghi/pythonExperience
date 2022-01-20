
number=input("please enter an Integer number: ")
length=len(number)
result=0
for i in range(length):
    result+=int(number[i])

print("Digits summation is: "+str(result))
