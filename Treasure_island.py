print('''
                                ######                                
                      ##########################.                     
                   ################################                   
                   ####      #######################                  
                   ####     .########################                 
                   ##################################                 
                   ##################################                 
                                    ###############((                 
      ###########################################((((  ,,,,,,,,,,,    
   ###########################################(((((((  ,,,,,,,,,,,,,  
  #########################################((((((((((  ,,,,,,,,,,,,,, 
 ########################################(((((((((((   ,,,,,,,,,,,,,,,
 #####################################(((((((((((((   ,,,,,,,,,,,,,,,,
####################################((((((((((((.    ,,,,,,,,,,,,,,,,,
#####################                             ,,,,,,,,,,,,,,,,,,,,
##################    ,******,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
 ################   *******,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
 ###############.  ******,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,
  ##############   ***,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,, 
   #############   *,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,  
     ###########   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,     
                   ,,,,,,,,,,,,,,,,,                                  
                   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,                 
                   ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,                 
                   ,,,,,,,,,,,,,,,,,,,,,,,,     ,,,,,                 
                   ,,,,,,,,,,,,,,,,,,,,,,,      ,,,,,                 
                    ,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,                  
                       ,,,,,,,,,,,,,,,,,,,,,,,,,,                     
''')
print("Welcome to Treasure Island\nYour mission is to find the treasure.")
choice=input("You\'re at a crossroad. Where do you want to go? Type \"Left\" or \"right\" \n")
if (choice.lower()=="left"):
       
       choice=input("You\'ve come to a lake.There is an island in the middle of the lake.\nType \"wait\" to wait for a boat.Type \"swim\" to swim across\n")
       if(choice.lower()=="wait"):
              choice=input("You are at the island ,there are 3 doors in front of you\n,witch door you are going to open ? \"Blue\" or \"Yellow\" or \"Red\"\n")
              if (choice.lower()=="yellow"):
                  print("You win the game congratulation")
              elif (choice=="red"):
                 print("You burned with huge fire, Game Over")
              elif(choice=="blue"):
                 print("You are surround with demons, Game Over") 
              else:
                     print("You lost your choice , Hasta la vista, baby , Game Over")
       else:
              print("Say your last hello to crocodiles,Game over")
else:
   print("You fell into a hole. Game Over")
