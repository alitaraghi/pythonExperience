print("Welcome to the Love Calculator")
name1=input("What is your name? \n")
name2=input("What is their name? \n")

combined_name=name1+name2
combine_name=combined_name.lower()
true_score=0
love_score=0


true_score+=combine_name.count("t")
true_score+=combine_name.count("r")
true_score+=combine_name.count("u")
true_score+=combine_name.count("e")
love_score+=combine_name.count("l")
love_score+=combine_name.count("o")
love_score+=combine_name.count("v")
love_score+=combine_name.count("e")
true_love_score=int(str(true_score)+str(love_score))


if (true_love_score<10) or (true_love_score>90):
    print(f"Your love score is {true_love_score},you go together like coke and mentose.")
elif(true_love_score>=40) and (true_love_score<=50):
    print(f"Your love score is {true_love_score},you are alright together")
else:
    print(f"youre love score is {true_love_score}")

