numbers=input("Input the list of number you want to find average!\n").split()
total=0
flag=0
#add all elements in list and count the size of list
for number in numbers:
    total+=int(number)
    flag+=1
#calculate average and round it by type casting    
average=int(total /flag)   
print("The average of numbers is: "+str(average))    