import random
from word_list import word_list
from HangManArts import stages
from os import system
#clear consol in windows lambda func creating
clear=lambda:system('cls')
#choose the random word
word=random.choice(word_list)
#print(word)
# make guess list
guess_list=[]
for char in range(len(word)):
    guess_list += "_"
   
#print(guess)

game_over=False
clear() 
while not game_over and len(stages)>0:
    
    guess=input("Enter your guess: ").lower()
    clear() 
    if guess in guess_list:
          print(f"You already guessed '{guess}'")
    right_guess=False
    for index in range(len(word)):
        char=word[index]
        if char==guess:
            guess_list[index]=guess
            right_guess=True
    if right_guess==False:
        print(stages.pop())            
    print(guess_list)
    if "_" not in guess_list:
        game_over=True 
        print("You Win!")
if len(stages)==0:
    print(f"The answer is : {word}\nYou lose!")      



              