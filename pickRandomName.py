from random import random


import random
name_list=input("Please Enter a bunch of name and seprate them by camma','  :\n")
name_list=name_list.split(",")
count_number=len(name_list)
picked_name=name_list[random.randint(0,count_number-1)]
print("The list you Enter: \n",name_list,"The picked name is:",picked_name)