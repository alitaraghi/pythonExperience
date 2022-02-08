import random
#drawing ascii art for hand gesture 
# Rock
rock="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissors="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
#get the user choice
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for scissors."))
#check if input is in defind range or not
if user_choice<0 or user_choice>2:
    print("You typed a wrong number,you lose")
else:
    #generte computer random choice    
    computer_choice=random.randint(0,2)
    #print the hand gesture of both choice
    if user_choice==0:
        print(rock)
    elif user_choice==1:
        print(paper)
    else:
        print(scissors)        
    print("\nComputer chose:\n")
    if computer_choice==0:
        print(rock)
    elif computer_choice==1:
        print(paper)
    else:
        print(scissors)
    #list of all possible form depend on user choice     
    winner_list=[["draw","lose","win"],["win","draw","lose"],["lose","win","draw"]]
    #pick the winner from winner_list
    result=winner_list[user_choice][computer_choice]
    #show result
    print(f"You {result}")    