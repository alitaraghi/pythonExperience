end_number=int(input("Please tell me the finall number of game: "))
#check if number divisible by 3 or 5 or both 3 and 5
for number in range(1,end_number):
    if number%15==0:
        print("fizzbuzz")
    elif number%5==0:
        print("buzz")
    elif number%3==0:
        print("fizz")
    else:
        print(number)            