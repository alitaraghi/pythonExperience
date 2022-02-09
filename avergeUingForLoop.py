numbers=input("Input the list of number you want to find average!\n").split()
total=0
list_size=0
#add all elements in list and count the size of list
for number in numbers:
    total+=int(number)
    list_size+=1
#calculate average and round it by type casting    
average=int(total /list_size)   
print("The average of numbers is: "+str(average))    