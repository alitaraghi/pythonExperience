numbers=input("Input the list of number you want to find average!\n").split()
max_num=min_num=int(numbers[0])
for number in numbers:
    if int(number)>max_num:
        max_num=int(number)
    elif int(number)<min_num:
        min_num=int(number)

print(f"The maximum of inputs is: {max_num}\nThe minimum of inputs is:{min_num} ")            
    