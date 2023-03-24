#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import time
def game():
    a=input("Do you want to start your journey?(Yes/No) : ")
    if a=="Yes":
        print("Okay, let's start your journey ;) ")
        print(" ")
        b=input("Please enter your name :")
        print(" ")
        print("Hey",b,", Get ready to fight with 'MAX' (The Pokemon master)")
        time.sleep(1)
        print("He has the strongest pokemon of em all(MEWTWO😈).You can defeat him by solving riddles and puzzles")
        print(" ")
        time.sleep(2.3)
        print("Max lives in town.You have to reach town by passing through jungle.")
        time.sleep(2.3)
        print("Currently you are in jungle, fight and catch few wild pokemon to defeat Max. You can catch them by solving puzzles.")
        print(" ")
        time.sleep(2.3)
        print("You have to catch upto 2 wild pokemons out of 3.")
        print("Maximum pokemon count is 3")
        time.sleep(2.3)
        c=input("So, In which region do you wanna play? (Unova / Kanto) : ")
        if c=="Unova":
            d = input("OHKAY! Now, Choose your starter Pokemon(Greyninja/Alakazam/Machamp) : ")            
            if d=="Greyninja":
                print("Hurray!! , Your choice is awesome. You got your 1st Pokemon or  buddy as 'Greyninja' ")
                print("Pokemon Count : 1")
                time.sleep(2.3)
                print("You are walking in Jungle and Boom!! a wild 'Raichu' appeared ")
                e=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")

                if e=="Catch":
                    print("Solve the puzzle to catch 'Raichu' ")
                    print("Guess the Movie")
                    k = input(" 🦁 + 👑  :  ")
                    

                    if k=="The Lion King":
                        print("GOTCHA!! You caught Raichu")
                        time.sleep(2.3)
                        print("Your Pokemon count increases by 1")
                        print("Pokemon Count : 2")
                        time.sleep(2.3)
                        print("You started walking again towards the town.....")
                        time.sleep(2.3)
                        print("BOOM!! a wild Ninetails appeared")
                        abc=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                        if abc=="Catch":
                            print("Solve this calculation to catch 'Ninetails' ")
                            acc= input( "12+687-43*45//3+12 : ")

                            if acc=="66" :
                                print("GOTCHA!! You caught Ninetails")
                                time.sleep(2.3)
                                print("Your Pokemon count increases by 1")
                                print("Pokemon Count : 3")
                                time.sleep(2.3)
                                print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                time.sleep(2.3)
                                print("Max -->  You can't defeat me even you have 10 pokemons")
                                time.sleep(2.3)
                                print(b, "---->HAHAHA.... What a joke! Let's wait and watch who will win")
                                time.sleep(2.3)
                                print("You both started the battle ")
                                print("Max has taken out the strongest pokemon  among all...MEWTWO")
                                
                                time.sleep(2.3)
                                print("Go Team",b, )
                                print("Solve this riddle to attack Mewtwo")
                                time.sleep(2.3)
                                govt = input("People buys me to eat but never eats me. Who am I?")
                                if govt =="Plate":
                                    print("Your team attacked Mewtwo")
                                    raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                    if raj=="Fearless Fire":
                                        time.sleep(2.3)
                                        print("WOW!!! This attack was Super effective , Mewtwo fainted")
                                        print("Victory belongs to you ^_^")
                                        print(" ")
                                        print("Restart to play again :) ")
                                        
                                        time.sleep(3)
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":

                                            
                                            
                                            print('''
                                              
                                              
------------------------------------------------------------------------------------------------------------------------
                                                 
                                                 
                                                    ''')
                                           
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()
                                    elif raj=="Tornado":
                        
                                        print("OHH!! Your attack was weak (●__●) ")
                                        print("Mewtwo attacked your team and your team fainted")
                                        time.sleep(2.3)
                                        print("You lose")
                                        print("Play again to take revenge")
                                        time.sleep(3)
                                        print(" ")
            
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''
                                              
                                              
----------------------------------------------------------------------------------------------------------------------
                                                 
                                                 
                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()
                                        
                                
                                    else:
                                        print("you chose a wrong option.Restart your game you fool")
                                        print(" ")
                        
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''
                                              
                                              
----------------------------------------------------------------------------------------------------------------
                                                 
                                                 
                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()



                                else:
                                    print("Mewtwo attacked your team and your team fainted")
                                    print("You lose")
                                    time.sleep(2.3)
                                    print("Play again to take revenge")
                                    print(" ")
                                    time.sleep(3)
                               
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''
                                              
                                              
-----------------------------------------------------------------------------------------------------------------------
                                                 
                                                 
                                                    ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()
                            else:
                                print("Ninetails disliked you.He attacked on you.You fainted")
                                time.sleep(2.3)
                                print("OHHH😩 You lost your game :( ")
                            
                                print("Restart to play again :) ")
                                print(" ")
                                time.sleep(2.3)
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''
                                              
                                              
--------------------------------------------------------------------------------------------------------------------
                                                 
                                                 
                                                    ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()

                        elif abc=="Leave":
                                print("Ohkay! Your choice, you will find more pokemons during this journey")
                                time.sleep(2.3)
                                print("You started walking again towards the town.....")
                                time.sleep(2.3)
                                print("BOOM!! a wild Gloom appeared")
                                q=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                                if q=="Catch":
                                    print("Arrange Jumbled Words to catch 'Gloom' ")
                                    r = input("N , E , S , B , I , G , N , E , R : ")
                                    if r=="BEGINNER":
                                        print("GOTCHA!! You caught Gloom ")
                                        print("Your Pokemon count increases by 1")
                                        print("Pokemon Count : 3")
                                        time.sleep(2.3)
                                        print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                        time.sleep(2.3)
                                        print("Max -->  You can't defeat me even you have 10 pokemons")
                                        time.sleep(2.3)
                                        print(b, " -->  HAHAHA.... What a joke! Let's wait and watch who will win")
                                        time.sleep(2.3)
                                        print("You both started the battle ")
                                        print("Max has taken out the strongest among all...MEWTWO")
                                        print("Go Team",b, )
                                        time.sleep(2.3)
                                        print("Solve this riddle to attack Mewtwo")
                                        qe = input("What five letter word becomes shorter when you add two letters to it : ")
                                        if govt =="Short":
                                            print("Your team attacked Mewtwo")
                                            raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                            if raj=="Fearless Fire":
                                                print("WOW!!! This attack was Super effective , Mewtwo fainted")
                                                print("Victory belongs to you ^_^")
                                                print(" ")
                                                print("Restart to play again :) ")
                                                print(" ")
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''
                                              
                                              
-------------------------------------------------------------------------------------------------------------------
                                                 
                                                 
                                                       ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()
                                            elif raj=="Tornado":
                                                print("OHH!! Your attack was weak (●__●) ")
                                                print("Mewtwo attacked your team and your team fainted")
                                                print("You lose")
                                                print("Play again to take revenge")
                                                print(" ")
                                                time.sleep(2.3)
                                                
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''

-------------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()
                                                
                                                
                                            else:
                                                print("you chose a wrong option.Restart your game you fool")
                                                print(" ")
                                                time.sleep(2.3)
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


-----------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()
                                        else:
                                            print("Mewtwo attacked your team and your team fainted")
                                            print("You lose")
                                            print("Play again to take revenge")
                                            print(" ")
                                            time.sleep(2.3)  
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                            


                                    else:
                                        print("Gloom disliked you.He attacked on you.You fainted")
                                        print("OHHH😩 You lost your game :( ")
                                        time.sleep(2.3)
                                        print("Restart to play again :) ")
                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''
                                              
                                              
-------------------------------------------------------------------------------------------------------------------
                                                 
                                                 
                                                    ''')
                                            game()
                                       
                                        else:
                                            print("Okay! Your choice")
                                            exit()



                                elif q=="Leave":
                                    print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")
                                    print("So you lost the game :( . Restart the game to play again")
                                    time.sleep(2.3)
                                    print(" ")
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


    -------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()

                                else:
                                    print("you chose a wrong option.Restart your game you fool")
                                    print(" ")
                                    time.sleep(2.3)
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


-----------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()


                        else:
                            print("you chose a wrong option.Restart your game you fool")
                            print(" ")
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


--------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()

                    else:
                        print("Raichu disliked you.He attacked on you.You fainted")
                        print("OHHH😩 You lost your game :( ")
                        print("Restart your game to play again")
                        print(" ")
                        time.sleep(2.3)
                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                        if re == "Yes":
                            print('''


    -----------------------------------------------------------------------------------------------------------------


                                    ''')
                            game()
                        else:
                            print("Okay! Your choice")
                            exit()

                elif e=="Leave":
                    print("Ohkay! Your choice, you will find more pokemons during this journey")
                    print("You started walking again towards the town.....")
                    time.sleep(2.3)
                    print("BOOM!! a wild Ninetails appeared")
                    ae=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                    if ae=="Catch":
                        print("Solve this calculation to catch 'Ninetails' ")
                        af = int(input(" 7! ?: "))

                        if af==5040:
                            print("GOTCHA!! You caught Ninetails ")
                            print("Your Pokemon count increases by 1")
                            print("Pokemon Count : 2")        
                            time.sleep(2.3)
                            print("You started walking again towards the town.....")
                            print("BOOM!! a wild Dragonite appeared")
                            ae=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                            if ae=="Catch":
                                print("Arrange these jumbled words to catch 'Dragonite' ")
                                af = input(" D , E , C , O , U , N , T , A ,I : ")
                                if af=="EDUCATION":
                                    print("GOTCHA!! You caught Dragonite ")
                                    print("Your Pokemon count increases by 1")
                                    print("Pokemon Count : 3")
                                    time.sleep(2.3)
                                    print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                    time.sleep(2.3)
                                    print("Max -->  You can't defeat me even you have 10 pokemons")
                                    time.sleep(2.3)
                                    print(b, " -->HAHAHA.... What a joke! Let's wait and watch who will win")
                                    time.sleep(2.3)
                                    print("You both started the battle ")
                                    print("Max has taken out the strongest among all...MEWTWO")
                                    print("Go Team",b, )
                                    time.sleep(2.3)
                                    print("Solve this riddle to attack Mewtwo")
                                    qr = input("I shoot but never kill. What am I?")
                                    if qe == "Camera":
                                        print("Your team attacked Mewtwo")
                                        raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                        if raj=="Fearless Fire":
                                            print("WOW!!! This attack was Super effective , Mewtwo fainted")
                                            print("Victory belongs to you ^_^")
                                            print(" ")
                                            print("Restart to play again :) ")
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


    ----------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                        elif raj=="Tornado":
                                            print("OHH!! Your attack was weak (●__●) ")
                                            print("Mewtwo attacked your team and your team fainted")
                                            print("You lose")
                                            print("Play again to take revenge")
                                            print(" ")
                                            time.sleep(2.3)
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


    ------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                        else:
                                            print("you chose a wrong option.Restart your game you fool")
                                            print(" ")
                                            time.sleep(2.3)
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


    --------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                    else:
                                        print("Mewtwo attacked your team and your team fainted")
                                        print("You lose")
                                        print("Play again to take revenge")
                                        print(" ")
                                        time.sleep(2.3)
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''
                                              
                                              
-------------------------------------------------------------------------------------------------------------------
                                                 
                                                 
                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()

                                else:
                                    print("Dragonite disliked you.He attacked on you.You fainted")
                                    print("OHHH😩 You lost your game :( ")
                                    print("Restart your game to play again")
                                    print(" ")
                                    time.sleep(2.3)
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


-------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()
                            elif ae=="Leave":
                                print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")
                                print("So you lost the game :( Restart the game to play again")
                                print(" ")
                                time.sleep(2.3)
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


--------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()
                            else:
                                print("you chose a wrong option.'YOU LOST' Restart your game you fool")
                                print(" ")
                                time.sleep(2.3)
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


--------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()

                        else:
                            print("Ninetails disliked you.He attacked on you.You fainted")
                            print("OHHH😩 You lost your game :( ")
                            print("Restart your game to play again")
                            print(" ")
                            time.sleep(2.3)
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


--------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()




                    elif ae=="Leave":
                            print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")
                            print("So you lost the game :( Restart the game to play again")
                            print(" ")
                            print("Restart to play again :) ")
                            print(" ")
                            time.sleep(2.3)
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


-----------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()

                    else:  
                        print("you chose a wrong option.'YOU LOST' Restart your game you fool") 
                        print(" ")
                        time.sleep(2.3)
                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                        if re == "Yes":
                            print('''


---------------------------------------------------------------------------------------------------------------------


                                    ''')
                            game()
                        else:
                            print("Okay! Your choice")
                            exit()
                         

                else:
                    print("you chose a wrong option.'YOU LOST' Restart your game you fool")
                    print(" ")
                    time.sleep(2.3)
                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                    if re == "Yes":
                        print('''


---------------------------------------------------------------------------------------------------------------------


                                ''')
                        game()
                    else:
                        print("Okay! Your choice")
                        exit()





            elif d=="Alakazam": 
                print("Hurray!! ,  Your choice is awesome. You got your 1st Pokemon or  buddy as 'Alakazam'")
                print("Pokemon Count : 1")
                time.sleep(2.3)
                print("You are walking in Jungle and Boom!! a wild 'Raichu' appeared ")
                e=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")

                if e=="Catch":
                    print("Solve the puzzle to catch 'Raichu' ")
                    print("Guess the Movie")
                    k = input("🪨 + ⭐ :  ")

                    if k=="Rockstar":
                        print("GOTCHA!! You caught Raichu")
                        print("Your Pokemon count increases by 1")
                        print("Pokemon Count : 2")
                        time.sleep(2.3)
                        print("You started walking again towards the town.....")
                        print("BOOM!! a wild Ninetails appeared")
                        abc=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                        if abc=="Catch":
                            print("Solve this calculation to catch 'Ninetails' ")
                            acc= input(" 69-4+34*2//5+100 : ")
                            if acc=="165":
                                print("GOTCHA!! You caught Ninetails")
                                print("Your Pokemon count increases by 1")
                                print("Pokemon Count : 3")
                                time.sleep(2.3)
                                print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                time.sleep(2.3)
                                print("Max -->  You can't defeat me even you have 10 pokemons")
                                time.sleep(2.3)
                                print(b, "---->HAHAHA.... What a joke! Let's wait and watch who will win")
                                time.sleep(2.3)
                                print("You both started the battle ")
                                print("Max has taken out the strongest among all...MEWTWO")
                                time.sleep(2.3)
                                print("Solve this riddle to attack Mewtwo")
                                govt = input("I have many keys but can't open a single lock. What is it")
                                if govt =="Piano":

                                    print("Your team attacked Mewtwo")

                                    raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                    if raj=="Fearless Fire":
                                        print("WOW!!! This attack was Super effective , Mewtwo fainted")
                                        print("Victory belongs to you ^_^")
                                        print(" ")
                                        print("Restart to play again :) ")
                                        print(" ")
                                        time.sleep(2.3)
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()
                                        
                                    elif raj=="Tornado":
                                        print("OHH!! Your attack was weak (●__●) ")
                                        print("Mewtwo attacked your team and your team fainted")
                                        print("You lose")
                                        print("Play again to take revenge")
                                        print(" ")
                                        time.sleep(2.3)
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()
                                    else:
                                        print("you chose a wrong option.Restart your game you fool")
                                        print(" ")
                                        time.sleep(2.3)
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()

                                else:
                                    print("Mewtwo attacked your team and your team fainted")
                                    print("You lose")
                                    print("Play again to take revenge")
                                    print(" ")
                                    time.sleep(2.3)
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()
                            else:
                                print("Ninetails disliked you.He attacked on you.You fainted")
                                time.sleep(2.3)
                                print("OHHH😩 You lost your game :( ")
                                print("Restart your game to play again")
                                print(" ")
                                time.sleep(2.3)
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()



                        elif abc=="Leave":
                                print("Ohkay! Your choice, you will find more pokemons during this journey")
                                print("You started walking again towards the town.....")
                                time.sleep(2.3)
                                print("BOOM!! a wild Gloom appeared")
                                q=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                                if q=="Catch":
                                    print("Arrange Jumbled Words to catch 'Gloom' ")
                                    r = input(" E , A , R , N ,T , O , F , O , N : ")
                                    if r=="AFTERNOON":
                                        print("GOTCHA!! You caught Gloom ")
                                        print("Your Pokemon count increases by 1")
                                        print("Pokemon Count : 3")
                                        time.sleep(2.3)
                                        print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                        time.sleep(2.3)
                                        print("Max -->  You can't defeat me even you have 10 pokemons")
                                        time.sleep(2.3)
                                        print(b, " -->  HAHAHA.... What a joke! Let's wait and watch who will win")
                                        time.sleep(2.3)
                                        print("You both started the battle ")
                                        print("Max has taken out the strongest among all...MEWTWO")
                                        print("Go Team",b, )
                                        time.sleep(2.3)
                                        print("Solve this riddle to attack Mewtwo")
                                        govt = input("You see me once in June, twice in November , and not at all in May. What is it?")
                                        if govt =="e":
                                            print("Your team attacked Mewtwo")

                                            raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                            if raj=="Fearless Fire":
                                                print("WOW!!! This attack was Super effective , Mewtwo fainted")
                                                print("Victory belongs to you ^_^")
                                                print(" ")
                                                print("Restart to play again :) ")
                                                print(" ")
                                                time.sleep(2.3)
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()
                                                
                                            elif raj=="Tornado":
                                                print("OHH!! Your attack was weak (●__●) ")
                                                print("Mewtwo attacked your team and your team fainted")
                                                print("You lose")
                                                time.sleep(2.3)
                                                print("Play again to take revenge")
                                                print(" ")
                                                time.sleep(2.3)
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()
                                            else:
                                                print("you chose a wrong option.Restart your game you fool")
                                                print(" ")
                                                time.sleep(2.3)
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()


                                        else:
                                            print("Mewtwo attacked your team and your team fainted")
                                            print("You lose")
                                            print("Play again to take revenge")
                                            print(" ")
                                            time.sleep(2.3)
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()


                                    else:
                                        print("Gloom disliked you.He attacked on you.You fainted")
                                        print("OHHH😩 You lost your game :( ")
                                        print("Restart your game to play again")
                                        print(" ")
                                        time.sleep(2.3)
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()



                                elif q=="Leave":
                                    
                                    print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")
                                    print("So you lost the game :( . Restart the game to play again")
                                    print(" ")
                                    time.sleep(2.3)
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()

                                else:
                                    print("you chose a wrong option.Restart your game you fool")
                                    print(" ")
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()


                        else:
                            print("you chose a wrong option.Restart your game you fool")
                            print(" ")
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


        ---------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()

                    else:
                        print("Raichu disliked you.He attacked on you.You fainted")
                        print("OHHH😩 You lost your game :( ")
                        print("Restart your game to play again")
                        print(" ")
                        time.sleep(2.3)
                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                        if re == "Yes":
                            print('''


    ---------------------------------------------------------------------------------------------------------------------


                                    ''')
                            game()
                        else:
                            print("Okay! Your choice")
                            exit()

                elif e=="Leave":
                    print("Ohkay! Your choice, you will find more pokemons during this journey")
                    print("You started walking again towards the town.....")
                    time.sleep(2.3)
                    print("BOOM!! a wild Ninetails appeared")
                    ae=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                    if ae=="Catch":
                        print("Find the missing number(?) to catch 'Ninetails' ")
                        af = int(input(" 2,3,6,4,5,20,?,3,18 : "))

                        if af==6:
                            print("GOTCHA!! You caught Ninetails ")
                            print("Your Pokemon count increases by 1")
                            print("Pokemon Count : 2")        
                            time.sleep(2.3)
                            print("You started walking again towards the town.....")
                            print("BOOM!! a wild Dragonite appeared")
                            ae=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                            if ae=="Catch":
                                print("Arrange these jumbled words to catch 'Dragonite' ")
                                af = input(" U , B , I , S , S , N , S , E : ")
                                if af=="BUSINESS":
                                    print("GOTCHA!! You caught Dragonite ")
                                    print("Your Pokemon count increases by 1")
                                    print("Pokemon Count : 3")
                                    print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                    time.sleep(2.3)
                                    print("Max -->  You can't defeat me even you have 10 pokemons")
                                    time.sleep(2.3)
                                    print(b, " -->HAHAHA.... What a joke! Let's wait and watch who will win")
                                    time.sleep(2.3)
                                    print("You both started the battle ")
                                    print("Max has taken out the strongest among all...MEWTWO")
                                    print("Go Team",b, )
                                    time.sleep(2.3)
                                    print("Solve this riddle to attack Mewtwo")
                                    govt = input("I can travel all around the world without leaving my corner. What is it?")
                                    if govt =="Stamp":
                                        print("Your team attacked Mewtwo")

                                        raj= input("Which attack do you want to do( Fearless Fire / Tornado )")
                                        if raj=="Fearless Fire":
                                            print("WOW!!! This attack was Super effective , Mewtwo fainted")
                                            print("Victory belongs to you ^_^")
                                            print(" ")
                                            print("Restart to play again :) ")
                                            print(" ")
                                            time.sleep(2.3)
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                        elif raj=="Tornado":
                                            print("OHH!! Your attack was weak (●__●) ")
                                            print("Mewtwo attacked your team and your team fainted")
                                            print("You lose")
                                            time.sleep(2.3)
                                            print("Play again to take revenge")
                                            print(" ")
                                            time.sleep(2.3)
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                        else:
                                            print("you chose a wrong option.Restart your game you fool")
                                            print(" ")
                                            print("Restart to play again :) ")
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                    else:
                                        print("Mewtwo attacked your team and your team fainted")
                                        print("You lose")
                                        print("Play again to take revenge")
                                        print(" ")
                                        time.sleep(2.3)
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()

                                else:
                                    print("Dragonite disliked you.He attacked on you.You fainted")
                                    print("OHHH😩 You lost your game :( ")
                                    print("Restart your game to play again")
                                    print(" ")
                                    time.sleep(2.3)
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()
                            elif ae=="Leave":
                                print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")
                                print("So you lost the game :( Restart the game to play again")
                                print(" ")
                                time.sleep(2.3)
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()
                            else:
                                print("you chose a wrong option.'YOU LOST' Restart your game you fool")
                                print(" ")
                                time.sleep(2.3)
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()

                        else:
                            print("Ninetails disliked you.He attacked on you.You fainted")
                            print("OHHH😩 You lost your game :( ")
                            print("Restart your game to play again")
                            print(" ")
                            time.sleep(2.3)
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


        ---------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()




                    elif ae=="Leave":
                            print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")
                            print("So you lost the game :( Restart the game to play again")
                            print(" ")
                            time.sleep(2.3)
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


        ---------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()

                    else:
                        print("you chose a wrong option.'YOU LOST' Restart your game you fool") 
                        print(" ")
                        time.sleep(2.3)
                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                        if re == "Yes":
                            print('''


    ---------------------------------------------------------------------------------------------------------------------


                                    ''')
                            game()
                        else:
                            print("Okay! Your choice")
                            exit()
                            

                else:
                    print("you chose a wrong option.'YOU LOST' Restart your game you fool")
                    print(" ")
                    time.sleep(2.3)
                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                    if re == "Yes":
                        print('''


---------------------------------------------------------------------------------------------------------------------


                                ''')
                        game()
                    else:
                        print("Okay! Your choice")
                        exit()


            elif d=="Machamp":
                print("Hurray!! , Your choice is awesome. You got your 1st Pokemon or  buddy as 'Machamp' ")
                print("Pokemon Count: 1")
                time.sleep(2.3)
                print("You are walking in Jungle and Boom!! a wild 'Raichu' appeared ")
                e=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")

                if e=="Catch":
                    print("Solve the puzzle to catch 'Raichu' ")
                    print("Guess the Movie")
                    k = input(" ✌➖✌ :  ")

                    if k=="Zero":
                        print("GOTCHA!! You caught Raichu")
                        print("Your Pokemon count increases by 1")
                        print("Pokemon Count : 2")
                        time.sleep(2.3)
                        print("You started walking again towards the town.....")
                        time.sleep(2.3)
                        print("BOOM!! a wild Ninetails appeared")
                        abc=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                        if abc=="Catch":
                            print("Find the missing number(?) to catch 'Ninetails' ")
                            acc= input("5,7,11,13,?,19,23 : ")
                            if acc=="17":
                                print("GOTCHA!! You caught Ninetails")
                                print("Your Pokemon count increases by 1")
                                print("Pokemon Count : 3")
                                time.sleep(2.3)
                                print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                time.sleep(2.3)
                                print("Max -->  You can't defeat me even you have 10 pokemons")
                                time.sleep(2.3)
                                print(b, "---->HAHAHA.... What a joke! Let's wait and watch who will win")
                                time.sleep(2.3)
                                print("You both started the battle ")
                                print("Max has taken out the strongest among all...MEWTWO")
                                print("Solve this riddle to attack Mewtwo")
                                time.sleep(2.3)
                                govt = input("You have to break me before you can use me. What is it?")
                                if govt =="Egg":
                                    print("Your team attacked Mewtwo")

                                    raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                    if raj=="Fearless Fire":
                                        print("WOW!!! This attack was Super effective , Mewtwo fainted")
                                        print("Victory belongs to you ^_^")
                                        print(" ")
                                        print("Restart to play again :) ")
                                        print(" ")
                                        time.sleep(2.3)
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()
                                    elif raj=="Tornado":
                                        print("OHH!! Your attack was weak (●__●) ")
                                        print("Mewtwo attacked your team and your team fainted")
                                        print("You lose")
                                        time.sleep(2.3)
                                        print("Play again to take revenge")
                                        print(" ")
                                        time.sleep(2.3)
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()
                                    else:
                                        print("you chose a wrong option.Restart your game you fool")
                                        print(" ")
                                        time.sleep(2.3)
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()
                                else:
                                    print("Mewtwo attacked your team and your team fainted")
                                    print("You lose")
                                    print("Play again to take revenge")
                                    print(" ")
                                    
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()






                            else:
                                print("Ninetails disliked you.He attacked on you.You fainted")
                                print("OHHH😩 You lost your game :( ")
                                time.sleep(2.3)
                                print("Restart to play again :) ")
                                print(" ")
                                time.sleep(2.3)
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()

                        elif abc=="Leave":
                                print("Ohkay! Your choice, you will find more pokemons during this journey")
                                print("You started walking again towards the town.....")
                                print("BOOM!! a wild Gloom appeared")
                                time.sleep(2.3)
                                q=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                                if q=="Catch":
                                    print("Arrange Jumbled Words to catch 'Gloom' ")
                                    r = input(" O , O , H , H , L , D , C , I , D : ")
                                    if r=="CHILDHOOD":
                                        print("GOTCHA!! You caught Gloom ")
                                        print("Your Pokemon count increases by 1")
                                        print("Pokemon Count : 3")
                                        time.sleep(2.3)
                                        print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                        time.sleep(2.3)
                                        print("Max -->  You can't defeat me even you have 10 pokemons")
                                        time.sleep(2.3)
                                        print(b, " -->  HAHAHA.... What a joke! Let's wait and watch who will win")
                                        time.sleep(2.3)
                                        print("You both started the battle ")
                                        print("Max has taken out the strongest among all...MEWTWO")
                                        print("Go Team",b, )
                                        time.sleep(2.3)
                                        print("Solve this riddle to attack Mewtwo")
                                        govt = input("Feed me and it will give me a life but give me a drink  and i will die. What am i?")
                                        if govt =="Fire":
                                            print("Your team attacked Mewtwo")

                                            raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                            if raj=="Fearless Fire":
                                                print("WOW!!! This attack was Super effective , Mewtwo fainted")
                                                print("Victory belongs to you ^_^")
                                                print(" ")
                                                print("Restart to play again :) ")
                                                print(" ")
                                                time.sleep(2.3)
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()
                                            elif raj=="Tornado":
                                                print("OHH!! Your attack was weak (●__●) ")
                                                print("Mewtwo attacked your team and your team fainted")
                                                print("You lose")
                                                time.sleep(2.3)
                                                print("Play again to take revenge")
                                                print(" ")
                                                time.sleep(2.3)
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()
                                            else:
                                                print("you chose a wrong option.Restart your game you fool")
                                                print(" ")
                                                time.sleep(2.3)
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()

                                        else:
                                            print("Mewtwo attacked your team and your team fainted")
                                            print("You lose")
                                            print("Play again to take revenge")
                                            print(" ")
                                            time.sleep(2.3)
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()





                                    else:
                                        print("Gloom disliked you.He attacked on you.You fainted")
                                        print("OHHH😩 You lost your game :( ")
                                        print("Restart to play again :) ")
                                        print(" ")
                                        time.sleep(2.3)
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()



                                elif q=="Leave":
                                    print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")
                                    print("So you lost the game :( . ")
                                    print(" ")
                                    print("Restart to play again :) ")
                                    print(" ")
                                    time.sleep(2.3)
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else: 
                                        print("Okay! Your choice")
                                        exit()

                                else:
                                    print("you chose a wrong option.Restart your game you fool")
                                    print(" ")
                                    time.sleep(2.3)
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                          
                                           print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                           game()
                                          
                                    else:
                                          
                                          print("Okay! Your choice")
                                          exit()


                        else:   
                                          
                            print("you chose a wrong option.Restart your game you fool")
                            print(" ")
                            time.sleep(2.3)
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


        ---------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()

                    else:
                        print("Raichu disliked you.He attacked on you.You fainted")
                        print("OHHH😩 You lost your game :( ")
                        print("Restart your game to play again")
                        print(" ")
                        print("Restart to play again :) ")
                        print(" ")
                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                        if re == "Yes":
                            print('''


    ---------------------------------------------------------------------------------------------------------------------


                                    ''')
                            game()
                        else:
                            print("Okay! Your choice")
                            exit()

                elif e=="Leave":
                    print("Ohkay! Your choice, you will find more pokemons during this journey")
                    print("You started walking again towards the town.....")
                    print("BOOM!! a wild Ninetails appeared")
                    ae=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                    if ae=="Catch":
                        print("Solve this calculation to catch 'Ninetails' ")
                        af = int(input("21+11+24-56+23*0: "))

                        if af==0:
                            print("GOTCHA!! You caught Ninetails")
                            print("Your Pokemon count increases by 1")
                            print("Pokemon Count : 2")        
                            print("You started walking again towards the town.....")
                            print("BOOM!! a wild Dragonite appeared")
                            ae=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                            if ae=="Catch":
                                print("Arrange these jumbled words to catch 'Dragonite' ")
                                af = input(" A , O , T , N , N , I , G , A , M , I , I : ")
                                if af=="IMAGINATION":
                                    print("GOTCHA!! You caught Dragonite ")
                                    print("Your Pokemon count increases by 1")
                                    print("Pokemon Count : 3")
                                    print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                    print("Max -->  You can't defeat me even you have 10 pokemons")
                                    print(b, " -->HAHAHA.... What a joke! Let's wait and watch who will win")
                                    print("You both started the battle ")
                                    print("Max has taken out the strongest among all...MEWTWO")
                                    print("Go Team",b, )
                                    print("Solve this riddle to attack Mewtwo")
                                    govt = input("I have four legs,but i can't walk. What am I?")
                                    if govt =="Table" or "Chair":
                                        print("Your team attacked Mewtwo")

                                        raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                        if raj=="Fearless Fire":
                                            print("WOW!!! This attack was Super effective , Mewtwo fainted")
                                            print("Victory belongs to you ^_^")
                                            print(" ")
                                            print("Restart to play again :) ")
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                        elif raj=="Tornado":
                                            print("OHH!! Your attack was weak (●__●) ")
                                            print("Mewtwo attacked your team and your team fainted")
                                            print("You lose")
                                            print("Play again to take revenge")
                                            print(" ")
                                            print("Restart to play again :) ")
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                        else:
                                            print("you chose a wrong option.Restart your game you fool")
                                            print(" ")
                                            print("Restart to play again :) ")
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                    else:
                                        print("Mewtwo attacked your team and your team fainted")
                                        print("You lose")
                                        print("Play again to take revenge")
                                        print(" ")
                                        print("Restart to play again :) ")
                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()




                                else:
                                        print("Dragonite disliked you.He attacked on you.You fainted")
                                        print("OHHH😩 You lost your game :( ")
                                        print("Restart your game to play again")
                                        print(" ")
                                        print("Restart to play again :) ")
                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()
                            elif ae=="Leave":
                                print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")
                                print("So you lost the game :( Restart the game to play again")
                                print(" ")
                                print("Restart to play again :) ")
                                print(" ")
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()
                            else:
                                print("you chose a wrong option.'YOU LOST' Restart your game you fool")
                                print(" ")
                                print("Restart to play again :) ")
                                print(" ")
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()

                        else:
                            print("Ninetails disliked you.He attacked on you.You fainted")
                            print("OHHH😩 You lost your game :( ")
                            print("Restart your game to play again")
                            print(" ")
                            print("Restart to play again :) ")
                            print(" ")
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


        ---------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()




                    elif ae=="Leave":
                            print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")
                            print("So you lost the game :( Restart the game to play again")
                            print(" ")
                            print("Restart to play again :) ")
                            print(" ")
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


        ---------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()

                    else:
                        print("you chose a wrong option.'YOU LOST' Restart your game you fool") 
                        print(" ")
                        print("Restart to play again :) ")
                        print(" ")
                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                        if re == "Yes":
                            print('''


    ---------------------------------------------------------------------------------------------------------------------


                                    ''')
                            game()
                        else:
                            print("Okay! Your choice")
                            exit()
                            

                else:
                    print("you chose a wrong option.'YOU LOST' Restart your game you fool")
                    print(" ")
                    print("Restart to play again :) ")
                    print(" ")
                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                    if re == "Yes":
                        print('''


---------------------------------------------------------------------------------------------------------------------


                                ''')
                        game()
                    else:
                        print("Okay! Your choice")
                        exit()
            else:
                print("you chose a wrong option.'YOU LOST' Restart your game you fool")
                print(" ")
                print("Restart to play again :) ")
                print(" ")
                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                if re == "Yes":
                    print('''


---------------------------------------------------------------------------------------------------------------------


                            ''')
                    game()
                else:
                    print("Okay! Your choice")
                    exit()

        elif c=="Kanto":
                e=input("OHKAY! Now, Choose your starter Pokemon(Charizard/Venasaur/Blastroise) :  ")
                if e=="Charizard":
                    print("Hurray!! , Your choice is awesome. You got your 1st Pokemon or  buddy as 'Charizard' ")
                    print("Pokemon Count : 1")
                    time.sleep(2.3)
                    print("You are walking in Jungle and Boom!! a wild 'Applin' appeared ")
                    time.sleep(2)
                    e=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")

                    if e=="Catch":
                        print("Solve the puzzle to catch 'Applin' ")
                        print("Guess the Movie")
                        k = input(" 🤼‍♂ + 👩👩  :  ")

                        if k=="Dangal":
                            print("GOTCHA!! You caught Applin")
                            print("Your Pokemon count increases by 1")
                            time.sleep(2.3)
                            print("Pokemon Count : 2")
                            time.sleep(2)
                            print("You started walking again towards the town.....")
                            time.sleep(2)
                            print("BOOM!! a wild Ninetails appeared")
                            time.sleep(2)
                            abc=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                            if abc=="Catch":
                                print("Solve this calculation to catch 'Ninetails' ")
                                acc= input("12+687-43*45//3+12 : ")
                                if acc=="66":
                                    print("GOTCHA!! You caught Ninetails")
                                    time.sleep(2)
                                    print("Your Pokemon count increases by 1")
                                    time.sleep(2)
                                    print("Pokemon Count : 3")
                                    time.sleep(2)
                                    print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                    time.sleep(2)
                                    print("Max -->  You can't defeat me even you have 10 pokemons")
                                    time.sleep(2)
                                    print(b, "---->HAHAHA.... What a joke! Let's wait and watch who will win")
                                    time.sleep(2)
                                    print("You both started the battle ")
                                    time.sleep(2)
                                    print("Max has taken out the strongest among all...MEWTWO")
                                    time.sleep(2)
                                    print("Solve this riddle to attack Mewtwo")
                                    time.sleep(2)
                                    govt = input("It's shorter than the rest , but when you're happy, you raise it up like it's the best. Who am I?")
                                    if govt =="Thumb":
                                        print("Your team attacked Mewtwo")
                                        time.sleep(2)
                                        raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                        if raj=="Fearless Fire":
                                            print("WOW!!! This attack was Super effective , Mewtwo fainted")
                                            print("Victory belongs to you ^_^")

                                            print(" ")
                                            print("Restart to play again :) ")
                                            time.sleep(2)
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                        elif raj=="Tornado":
                                            print("OHH!! Your attack was weak (●__●) ")

                                            print("Mewtwo attacked your team and your team fainted")
                                            print("You lose")

                                            print("Play again to take revenge")

                                            print(" ")
                                            print("Restart to play again :) ")
                                            time.sleep(2)
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                        else:
                                            print("you chose a wrong option.Restart your game you fool")
                                            time.sleep(2)
                                            print(" ")
                                            print("Restart to play again :) ")
                                            time.sleep(2)
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()

                                    else:
                                        print("Mewtwo attacked your team and your team fainted")

                                        print("You lose")

                                        print("Play again to take revenge")
                                        time.sleep(2)
                                        print(" ")
                                        print("Restart to play again :) ")
                                        time.sleep(2)
                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()




                                else:
                                    print("Ninetails disliked you.He attacked on you.You fainted")

                                    print("OHHH😩 You lost your game :( ")
                                    time.sleep(2)
                                    print("Restart your game to play again")
                                    time.sleep(2)
                                    print(" ")
                                    print("Restart to play again :) ")
                                    time.sleep(2)
                                    print(" ")
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()

                            elif abc=="Leave":
                                    print("Ohkay! Your choice, you will find more pokemons during this journey")
                                    time.sleep(2)
                                    print("You started walking again towards the town.....")
                                    time.sleep(2)
                                    print("BOOM!! a wild Gloom appeared")
                                    time.sleep(2)
                                    q=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                                    if q=="Catch":
                                        print("Arrange Jumbled Words to catch 'Gloom' ")

                                        r = input(" B , L , E , C , N , M , A , U , A : ")
                                        if r=="AMBULANCE":
                                            print("GOTCHA!! You caught Gloom ")
                                            time.sleep(2)
                                            print("Your Pokemon count increases by 1")

                                            print("Pokemon Count : 3")
                                            time.sleep(2)
                                            print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                            time.sleep(2)
                                            print("Max -->  You can't defeat me even you have 10 pokemons")
                                            time.sleep(2)
                                            print(b, " -->  HAHAHA.... What a joke! Let's wait and watch who will win")
                                            time.sleep(2)
                                            print("You both started the battle ")
                                            time.sleep(2)
                                            print("Max has taken out the strongest among all...MEWTWO")
                                            time.sleep(2)
                                            print("Go Team",b, )
                                            time.sleep(2)
                                            print("Solve this riddle to attack Mewtwo")
                                            govt = input("What's green but not a leaf , copies other but is not a monkey?")
                                            if govt =="Parrot":
                                                print("Your team attacked Mewtwo")
                                                time.sleep(2)
                                                raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                                if raj=="Fearless Fire":
                                                    print("WOW!!! This attack was Super effective , Mewtwo fainted")

                                                    print("Victory belongs to you ^_^")

                                                    print(" ")
                                                    print("Restart to play again :) ")
                                                    time.sleep(2)
                                                    print(" ")
                                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                    if re == "Yes":
                                                        print('''


                                ---------------------------------------------------------------------------------------------------------------------


                                                                ''')
                                                        game()
                                                    else:
                                                        print("Okay! Your choice")
                                                        exit()
                                                elif raj=="Tornado":
                                                    print("OHH!! Your attack was weak (●__●) ")

                                                    print("Mewtwo attacked your team and your team fainted")

                                                    print("You lose")

                                                    print("Play again to take revenge")

                                                    print(" ")
                                                    print("Restart to play again :) ")
                                                    time.sleep(2)
                                                    print(" ")
                                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                    if re == "Yes":
                                                        print('''


                                ---------------------------------------------------------------------------------------------------------------------


                                                                ''')
                                                        game()
                                                    else:
                                                        print("Okay! Your choice")
                                                        exit()
                                                else:
                                                    print("you chose a wrong option.Restart your game you fool")
                                                    time.sleep(2)
                                                    print(" ")
                                                    print("Restart to play again :) ")
                                                    time.sleep(2)
                                                    print(" ")
                                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                    if re == "Yes":
                                                        print('''


                                ---------------------------------------------------------------------------------------------------------------------


                                                                ''')
                                                        game()
                                                    else:
                                                        print("Okay! Your choice")
                                                        exit()
                                            else:
                                                print("Mewtwo attacked your team and your team fainted")

                                                print("You lose")

                                                print("Play again to take revenge")

                                                print(" ")
                                                print("Restart to play again :) ")
                                                time.sleep(2)
                                                print(" ")
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()



                                        else:
                                            print("Gloom disliked you.He attacked on you.You fainted")


                                            print("OHHH😩 You lost your game :( ")

                                            print("Restart your game to play again")

                                            print(" ")
                                            print("Restart to play again :) ")
                                            time.sleep(2)
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()



                                    elif q=="Leave":
                                        print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")
                                        time.sleep(2)
                                        print("So you lost the game :( . Restart the game to play again")

                                        print(" ")
                                        print("Restart to play again :) ")

                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()

                                    else:
                                        print("you chose a wrong option.Restart your game you fool")

                                        print(" ")
                                        print("Restart to play again :) ")
                                        time.sleep(2)
                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()


                            else:
                                print("you chose a wrong option.Restart your game you fool")

                                print(" ")
                                print("Restart to play again :) ")

                                print(" ")
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                time.sleep(2)
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()

                        else:
                            print("Raichu disliked you.He attacked on you.You fainted")

                            print("OHHH😩 You lost your game :( ")

                            print("Restart your game to play again")

                            print(" ")
                            print("Restart to play again :) ")
                            time.sleep(2)
                            print(" ")
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


        ---------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()

                    elif e=="Leave":
                        print("Ohkay! Your choice, you will find more pokemons during this journey")
                        time.sleep(2)
                        print("You started walking again towards the town.....")
                        time.sleep(2)
                        print("BOOM!! a wild Ninetails appeared")
                        time.sleep(2)
                        ae=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                        if ae=="Catch":
                            print("Solve this calculation to catch 'Ninetails' ")
                            af = int(input("2,7,12,17,?,27 : "))

                            if af==22:
                                print("GOTCHA!! You caught Ninetails ")
                                time.sleep(2)
                                print("Your Pokemon count increases by 1")
                                time.sleep(2)
                                print("Pokemon Count : 2")  
                                time.sleep(2)
                                print("You started walking again towards the town.....")
                                time.sleep(2)
                                print("BOOM!! a wild Dragonite appeared")
                                ae=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                                if ae=="Catch":
                                    print("Arrange these jumbled words to catch 'Dragonite' ")
                                    af = input(" N , N , L , N , R , E , I , I , T , O , A , T , A  : ")
                                    if af=="INTERNATIONAL":
                                        print("GOTCHA!! You caught Dragonite ")
                                        time.sleep(2)
                                        print("Your Pokemon count increases by 1")
                                        time.sleep(2)
                                        print("Pokemon Count : 3")
                                        time.sleep(2)
                                        print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                        time.sleep(2)
                                        print("Max -->  You can't defeat me even you have 10 pokemons")
                                        time.sleep(2)
                                        print(b, " -->HAHAHA.... What a joke! Let's wait and watch who will win")
                                        time.sleep(2)
                                        print("You both started the battle ")
                                        time.sleep(2)
                                        print("Max has taken out the strongest among all...MEWTWO")
                                        time.sleep(2)
                                        print("Go Team",b, )
                                        time.sleep(2)
                                        print("Max has taken out the strongest among all...MEWTWO")
                                        time.sleep(2)
                                        print("Solve this riddle to attack Mewtwo")
                                        govt = input("I’m tall when I’m young, and I’m short when I’m old. What am I?")
                                        if govt =="Candle" or govt == "Pencil":
                                            print("Your team attacked Mewtwo")

                                            raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                            if raj=="Fearless Fire":
                                                print("WOW!!! This attack was Super effective , Mewtwo fainted")

                                                print("Victory belongs to you ^_^")

                                                print(" ")
                                                print("Restart to play again :) ")
                                                time.sleep(2)
                                                print(" ")
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()
                                            elif raj=="Tornado":
                                                print("OHH!! Your attack was weak (●__●) ")


                                                print("Mewtwo attacked your team and your team fainted")

                                                print("You lose")

                                                print("Play again to take revenge")

                                                print(" ")
                                                print("Restart to play again :) ")
                                                time.sleep(2)
                                                print(" ")
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()
                                            else:
                                                print("you chose a wrong option.Restart your game you fool")

                                                print(" ")
                                                print("Restart to play again :) ")

                                                print(" ")
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()



                                        else:
                                            print("Mewtwo attacked your team and your team fainted")

                                            print("You lose")

                                            print("Play again to take revenge")

                                            print(" ")
                                            print("Restart to play again :) ")
                                            time.sleep(2)
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()


                                    else:
                                        print("Dragonite disliked you.He attacked on you.You fainted")

                                        print("OHHH😩 You lost your game :( ")

                                        print("Restart your game to play again")

                                        print(" ")
                                        print("Restart to play again :) ")
                                        time.sleep(2)
                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()
                                elif ae=="Leave":
                                    print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")
                                    time.sleep(2)
                                    print("So you lost the game :( Restart the game to play again")

                                    print(" ")
                                    print("Restart to play again :) ")

                                    print(" ")
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()
                                else:
                                    print("you chose a wrong option.'YOU LOST' Restart your game you fool")

                                    print(" ")
                                    print("Restart to play again :) ")

                                    print(" ")
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()

                            else:
                                print("Ninetails disliked you.He attacked on you.You fainted")

                                print("OHHH😩 You lost your game :( ")

                                print("Restart your game to play again")

                                print(" ")
                                print("Restart to play again :) ")
                                time.sleep(2)
                                print(" ")
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()




                        elif ae=="Leave":
                                print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")
                                time.sleep(2)
                                print("So you lost the game :( Restart the game to play again")

                                print(" ")
                                print("Restart to play again :) ")

                                print(" ")
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()

                        else:
                            print("you chose a wrong option.'YOU LOST' Restart your game you fool")

                            print(" ")
                            print("Restart to play again :) ")

                            print(" ")
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


        ---------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()



                    else:
                        print("you chose a wrong option.'YOU LOST' Restart your game you fool")

                        print(" ")
                        print("Restart to play again :) ")

                        print(" ")
                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                        if re == "Yes":
                            print('''


        ---------------------------------------------------------------------------------------------------------------------


                                    ''')
                            game()
                        else:
                            print("Okay! Your choice")
                            exit()




                elif e=="Venasaur":
                    print("Hurray!! , Your choice is awesome. You got your 1st Pokemon or  buddy as 'Venasaur' ")
                    time.sleep(2)
                    print("Pokemon Count : 1")
                    time.sleep(2)
                    print("You are walking in Jungle and Boom!! a wild 'Raichu' appeared ")
                    time.sleep(2)
                    e=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")


                    if e=="Catch":
                        print("Solve the puzzle to catch 'Raichu' ")
                        print("Guess the Movie")
                        k = input(" 🧪 + 💡  :  ")

                        if k=="Tubelight":
                            print("GOTCHA!! You caught Raichu")
                            time.sleep(2)
                            print("Your Pokemon count increases by 1")
                            time.sleep(2)
                            print("Pokemon Count : 2")
                            time.sleep(2)
                            print("You started walking again towards the town.....")  
                            time.sleep(2)
                            print("BOOM!! a wild Ninetails appeared")            
                            abc=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                            if abc=="Catch":
                                print("Solve this calculation to catch 'Ninetails' ")
                                acc= input("12+687-43*45//3+12 : ")
                                if acc=="66":
                                    print("GOTCHA!! You caught Ninetails")
                                    time.sleep(2)
                                    print("Your Pokemon count increases by 1")
                                    time.sleep(2)
                                    print("Pokemon Count : 3")
                                    time.sleep(2)
                                    print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                    time.sleep(2)
                                    print("Max -->  You can't defeat me even you have 10 pokemons")
                                    time.sleep(2)
                                    print(b, "---->HAHAHA.... What a joke! Let's wait and watch who will win")
                                    time.sleep(2)
                                    print("You both started the battle ")
                                    time.sleep(2)
                                    print("Max has taken out the strongest among all...MEWTWO")
                                    time.sleep(2)
                                    print("Solve this riddle to attack mewtwo")
                                    govt = input("Take off my skin and I won’t cry, but you will! What am I?")
                                    if govt =="Onion":
                                        raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                        if raj=="Fearless Fire":
                                            print("WOW!!! This attack was Super effective , Mewtwo fainted")

                                            print("Victory belongs to you ^_^")
                                            print(" ")

                                            print("Restart to play again :) ")
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                        elif raj=="Tornado":
                                            print("OHH!! Your attack was weak (●__●) ")

                                            print("Mewtwo attacked your team and your team fainted")

                                            print("You lose")

                                            print("Play again to take revenge")

                                            print(" ")
                                            print("Restart to play again :) ")

                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                        else:
                                            print("you chose a wrong option.Restart your game you fool")
                                            print(" ")

                                            print("Restart to play again :) ")

                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()



                                    else:
                                        print("Mewtwo attacked your team and your team fainted")

                                        print("You lose")

                                        print("Play again to take revenge")

                                        print(" ")
                                        print("Restart to play again :) ")

                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()

                                else:
                                    print("Ninetails disliked you.He attacked on you.You fainted")

                                    print("OHHH😩 You lost your game :( ")

                                    print("Restart your game to play again")

                                    print(" ")
                                    print("Restart to play again :) ")

                                    print(" ")
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()

                            elif abc=="Leave":
                                    print("Ohkay! Your choice, you will find more pokemons during this journey")
                                    time.sleep(2)
                                    print("You started walking again towards the town.....")
                                    time.sleep(2)
                                    print("BOOM!! a wild Gloom appeared")
                                    time.sleep(2)
                                    q=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                                    if q=="Catch":
                                        print("Arrange Jumbled Words to catch 'Gloom' ")
                                        r = input("T,O,P,O,T,A : ")
                                        if r=="POTATO":
                                            print("GOTCHA!! You caught Gloom ")
                                            time.sleep(2)
                                            print("Your Pokemon count increases by 1")
                                            time.sleep(2)
                                            print("Pokemon Count : 3")
                                            time.sleep(2)
                                            print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                            time.sleep(2)
                                            print("Max -->  You can't defeat me even you have 10 pokemons")
                                            time.sleep(2)
                                            print(b, " -->  HAHAHA.... What a joke! Let's wait and watch who will win")
                                            time.sleep(2)
                                            print("You both started the battle ")
                                            time.sleep(2)
                                            print("Max has taken out the strongest among all...MEWTWO")
                                            time.sleep(2)
                                            print("Go Team",b, )
                                            time.sleep(2)
                                            print("Solve this riddle to win the battle")
                                            qe = input("I have 13 hearts, but no other organs? What am I?")
                                            if qe=="Cards":
                                                raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                                if raj=="Fearless Fire":
                                                    print("WOW!!! This attack was Super effective , Mewtwo fainted")

                                                    print("Victory belongs to you ^_^")

                                                    print(" ")
                                                    print("Restart to play again :) ")

                                                    print(" ")
                                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                    if re == "Yes":
                                                        print('''


                                ---------------------------------------------------------------------------------------------------------------------


                                                                ''')
                                                        game()
                                                    else:
                                                        print("Okay! Your choice")
                                                        exit()
                                                elif raj=="Tornado":
                                                    print("OHH!! Your attack was weak (●__●) ")

                                                    print("Mewtwo attacked your team and your team fainted")

                                                    print("You lose")

                                                    print("Play again to take revenge")

                                                    print(" ")
                                                    print("Restart to play again :) ")

                                                    print(" ")
                                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                    if re == "Yes":
                                                        print('''


                                ---------------------------------------------------------------------------------------------------------------------


                                                                ''')
                                                        game()
                                                    else:
                                                        print("Okay! Your choice")
                                                        exit()
                                                else:
                                                    print("you chose a wrong option.Restart your game you fool")

                                                    print(" ")

                                                    print("Restart to play again :) ")

                                                    print(" ")
                                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                    if re == "Yes":
                                                        print('''


                                ---------------------------------------------------------------------------------------------------------------------


                                                                ''')
                                                        game()
                                                    else:
                                                        print("Okay! Your choice")
                                                        exit()


                                            else:
                                                print("Mewtwo attacked your team and your team fainted")

                                                print("You lose")

                                                print("Play again to take revenge")

                                                print(" ")

                                                print("Restart to play again :) ")

                                                print(" ")
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()

                                        else:
                                            print("Gloom disliked you.He attacked on you.You fainted")

                                            print("OHHH😩 You lost your game :( ")

                                            print("Restart your game to play again")

                                            print(" ")
                                            print("Restart to play again :) ")
                                            time.sleep(2)
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()



                                    elif q=="Leave":
                                        print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")

                                        print("So you lost the game :( . Restart the game to play again")

                                        print(" ")

                                        print("Restart to play again :) ")

                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()


                                    else:
                                        print("you chose a wrong option.Restart your game you fool")

                                        print(" ")

                                        print("Restart to play again :) ")

                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()


                            else:
                                print("you chose a wrong option.Restart your game you fool")

                                print(" ")

                                print("Restart to play again :) ")

                                print(" ")
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()


                        else:
                            print("Raichu disliked you.He attacked on you.You fainted")

                            print("OHHH😩 You lost your game :( ")

                            print("Restart your game to play again")

                            print(" ")

                            print("Restart to play again :) ")

                            print(" ")
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


        ---------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()

                    elif e=="Leave":
                        print("Ohkay! Your choice, you will find more pokemons during this journey")
                        time.sleep(2)
                        print("You started walking again towards the town.....")
                        time.sleep(2)
                        print("BOOM!! a wild Ninetails appeared")
                        time.sleep(2)
                        ae=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                        if ae=="Catch":
                            print("Solve this calculation to catch 'Ninetails' ")
                            af = int(input("12+685-43*45//3+12 : "))

                            if af==66:
                                print("GOTCHA!! You caught Ninetails ")
                                time.sleep(2)
                                print("Your Pokemon count increases by 1")
                                time.sleep(2)
                                print("Pokemon Count : 2")
                                time.sleep(2)
                                print("You started walking again towards the town.....")
                                time.sleep(2)
                                print("BOOM!! a wild Dragonite appeared")
                                time.sleep(2)
                                ae=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                                if ae=="Catch":
                                    print("Arrange these jumbled words to catch 'Dragonite' ")
                                    af = input("N,T,O,T,C,O : ")
                                    if af=="COTTON":
                                        print("GOTCHA!! You caught Dragonite ")
                                        time.sleep(2)
                                        print("Your Pokemon count increases by 1")
                                        time.sleep(2)
                                        print("Pokemon Count : 3")
                                        time.sleep(2)
                                        print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                        time.sleep(2)
                                        print("Max -->  You can't defeat me even you have 10 pokemons")
                                        time.sleep(2)
                                        print(b, " -->HAHAHA.... What a joke! Let's wait and watch who will win")
                                        time.sleep(2)
                                        print("You both started the battle ")
                                        time.sleep(2)
                                        print("Max has taken out the strongest among all...MEWTWO")
                                        time.sleep(2)
                                        print("Go Team",b, )
                                        print("Solve this riddle to win the battle")
                                        qr = input("I have a head and a tail that will never meet. Having too many of me is always a treat. What am I?")
                                        if qe == "Coin":
                                            raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                            if raj=="Fearless Fire":
                                                print("WOW!!! This attack was Super effective , Mewtwo fainted")

                                                print("Victory belongs to you ^_^")

                                                print(" ")

                                                print("Restart to play again :) ")
                                                time.sleep(2)
                                                print(" ")
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()
                                            elif raj=="Tornado":
                                                print("OHH!! Your attack was weak (●__●) ")

                                                print("Mewtwo attacked your team and your team fainted")

                                                print("You lose")

                                                print("Play again to take revenge")  
                                                print(" ")

                                                print("Restart to play again :) ")
                                                print(" ")
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()
                                            else:
                                                print("you chose a wrong option.Restart your game you fool")

                                                print(" ")

                                                print("Restart to play again :) ")
                                                print(" ")
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()

                                        else:
                                            print("Mewtwo attacked your team and your team fainted")
                                            print("You lose")

                                            print("Play again to take revenge")

                                            print(" ")

                                            print("Restart to play again :) ")

                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()


                                    else:
                                        print("Dragonite disliked you.He attacked on you.You fainted")

                                        print("OHHH😩 You lost your game :( ")

                                        print("Restart your game to play again")

                                        print(" ")

                                        print("Restart to play again :) ")

                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()
                                elif ae=="Leave":
                                    print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")

                                    print("So you lost the game :( Restart the game to play again")

                                    print(" ")

                                    print("Restart to play again :) ")
                                    time.sleep(2)
                                    print(" ")
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()
                                else:
                                    print("you chose a wrong option.'YOU LOST' Restart your game you fool")
                                    time.sleep(2)
                                    print(" ")

                                    print("Restart to play again :) ")
                                    time.sleep(2)
                                    print(" ")
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()

                            else:
                                print("Ninetails disliked you.He attacked on you.You fainted")

                                print("OHHH😩 You lost your game :( ")

                                print("Restart your game to play again")

                                print(" ")

                                print("Restart to play again :) ")

                                print(" ")
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()




                        elif ae=="Leave":
                                print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")

                                print("So you lost the game :( Restart the game to play again")

                                print(" ")
                                print("Restart to play again :) ")

                                print(" ")
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()

                        else:
                            print("you chose a wrong option.'YOU LOST' Restart your game you fool")

                            print(" ")

                            print("Restart to play again :) ")

                            print(" ")
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


        ---------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()


                    else:
                        print("you chose a wrong option.'YOU LOST' Restart your game you fool")

                        print(" ")

                        print("Restart to play again :) ")

                        print(" ")
                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                        if re == "Yes":
                            print('''


    ---------------------------------------------------------------------------------------------------------------------


                                    ''')
                            game()
                        else:
                            print("Okay! Your choice")
                            exit()

                elif e=="Blastroise":
                    print("Hurray!! , Your choice is awesome. You got your 1st Pokemon or  buddy as 'Blastroise' ")
                    time.sleep(2)
                    print("Pokemon Count : 1")
                    time.sleep(2)
                    print("You are walking in Jungle and Boom!! a wild 'Raichu' appeared ")
                    time.sleep(2)
                    e=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")

                    if e=="Catch":
                        print("Solve the puzzle to catch 'Raichu' ")
                        print("Guess the Movie")
                        k = input(" 📄 + 1️⃣5️⃣  :  ")

                        if k=="Article 15":
                            print("GOTCHA!! You caught Raichu")
                            time.sleep(2)
                            print("Your Pokemon count increases by 1")
                            time.sleep(2)
                            print("Pokemon Count : 2")
                            time.sleep(2)
                            print("You started walking again towards the town.....")
                            time.sleep(2)
                            print("BOOM!! a wild Ninetails appeared")
                            abc=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                            if abc=="Catch":
                                print("Solve this calculation to catch 'Ninetails' ")
                                acc= input("12+687-43*45//3+12 : ")
                                if acc=="66":
                                    print("GOTCHA!! You caught Ninetails")
                                    time.sleep(2)
                                    print("Your Pokemon count increases by 1")
                                    time.sleep(2)
                                    print("Pokemon Count : 3")
                                    time.sleep(2)
                                    print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                    time.sleep(2)
                                    print("Max -->  You can't defeat me even you have 10 pokemons")
                                    time.sleep(2)
                                    print(b, "---->HAHAHA.... What a joke! Let's wait and watch who will win")
                                    time.sleep(2)
                                    print("You both started the battle ")
                                    time.sleep(2)
                                    print("Max has taken out the strongest among all...MEWTWO")
                                    time.sleep(2)
                                    print("Solve this riddle to defeat max")
                                    govt = input("I can fly but have no wings. I can cry but I have no eyes. Wherever I go, darkness follows me. What am I?")
                                    if govt =="Clouds":
                                        raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                        if raj=="Fearless Fire":
                                            print("WOW!!! This attack was Super effective , Mewtwo fainted")

                                            print("Victory belongs to you ^_^")

                                            print(" ")

                                            print("Restart to play again :) ")
                                            time.sleep(2)
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                        elif raj=="Tornado":
                                            print("OHH!! Your attack was weak (●__●) ")

                                            print("Mewtwo attacked your team and your team fainted")

                                            print("You lose")

                                            print("Play again to take revenge")

                                            print(" ")

                                            print("Restart to play again :) ")
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()
                                        else:
                                            print("you chose a wrong option.Restart your game you fool")

                                            print(" ")

                                            print("Restart to play again :) ")
                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()


                                    else:
                                        print("Mewtwo attacked your team and your team fainted")

                                        print("You lose")

                                        print("Play again to take revenge")

                                        print(" ")
                                        print("Restart to play again :) ")
                                        time.sleep(2)
                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()

                                else:
                                    print("Ninetails disliked you.He attacked on you.You fainted")

                                    print("OHHH😩 You lost your game :( ")

                                    print("Restart your game to play again")

                                    print(" ")
                                    print("Restart to play again :) ")
                                    
                                    print(" ")
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()

                            elif abc=="Leave":
                                    print("Ohkay! Your choice, you will find more pokemons during this journey")
                                    time.sleep(2)
                                    print("You started walking again towards the town.....")
                                    time.sleep(2)
                                    print("BOOM!! a wild Gloom appeared")
                                    time.sleep(2)
                                    q=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                                    if q=="Catch":
                                        print("Arrange Jumbled Words to catch 'Gloom' ")
                                        r = input("M , T , O , I , G , R , N , I , A : ")
                                        if r=="MIGRATION":
                                            print("GOTCHA!! You caught Gloom ")
                                            time.sleep(2)
                                            print("Your Pokemon count increases by 1")
                                            time.sleep(2)
                                            print("Pokemon Count : 3")
                                            time.sleep(2)
                                            print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                            time.sleep(2)
                                            print("Max -->  You can't defeat me even you have 10 pokemons")
                                            time.sleep(2)
                                            print(b, " -->  HAHAHA.... What a joke! Let's wait and watch who will win")
                                            time.sleep(2)
                                            print("You both started the battle ")
                                            time.sleep(2)
                                            print("Max has taken out the strongest among all...MEWTWO")
                                            time.sleep(2)
                                            print("Go Team",b, )
                                            time.sleep(2)
                                            print("Solve this riddle to win the battle")
                                            qe = input("I follow you all the time and copy your every move, but you can’t touch me or catch me. What am I?")
                                            if qe=="Shadow":
                                                raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                                if raj=="Fearless Fire":
                                                    print("WOW!!! This attack was Super effective , Mewtwo fainted")

                                                    print("Victory belongs to you ^_^")

                                                    print(" ")
                                                    print("Restart to play again :) ")

                                                    print(" ")
                                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                    if re == "Yes":
                                                        print('''


                                ---------------------------------------------------------------------------------------------------------------------


                                                                ''')
                                                        game()
                                                    else:
                                                        print("Okay! Your choice")
                                                        exit()
                                                elif raj=="Tornado":
                                                    print("OHH!! Your attack was weak (●__●) ")

                                                    print("Mewtwo attacked your team and your team fainted")

                                                    print("You lose")

                                                    print("Play again to take revenge")

                                                    print(" ")
                                                    print("Restart to play again :) ")
                                                    print(" ")
                                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                    if re == "Yes":
                                                        print('''


                                ---------------------------------------------------------------------------------------------------------------------


                                                                ''')
                                                        game()
                                                    else:
                                                        print("Okay! Your choice")
                                                        exit()
                                                else:
                                                    print("you chose a wrong option.Restart your game you fool")

                                                    print(" ")
                                                    print("Restart to play again :) ")

                                                    print(" ")
                                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                    if re == "Yes":
                                                        print('''


                                ---------------------------------------------------------------------------------------------------------------------


                                                                ''')
                                                        game()
                                                    else:
                                                        print("Okay! Your choice")
                                                        exit()

                                            else:
                                                print("Mewtwo attacked your team and your team fainted")

                                                print("You lose")

                                                print("Play again to take revenge")

                                                print(" ")
                                                print("Restart to play again :) ")

                                                print(" ")
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()


                                        else:
                                            print("Gloom disliked you.He attacked on you.You fainted")

                                            print("OHHH😩 You lost your game :( ")

                                            print("Restart your game to play again")

                                            print(" ")
                                            print("Restart to play again :) ")

                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()



                                    elif q=="Leave":
                                        print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")

                                        print("So you lost the game :( . Restart the game to play again")

                                        print(" ")
                                        print("Restart to play again :) ")

                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()

                                    else:
                                        print("you chose a wrong option.Restart your game you fool")

                                        print(" ")
                                        print("Restart to play again :) ")

                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()


                            else:
                                print("you chose a wrong option.Restart your game you fool")

                                print(" ")
                                print("Restart to play again :) ")

                                print(" ")
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()

                        else:
                            print("Raichu disliked you.He attacked on you.You fainted")

                            print("OHHH😩 You lost your game :( ")

                            print("Restart your game to play again")

                            print(" ")
                            print("Restart to play again :) ")

                            print(" ")
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


        ---------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()

                    elif e=="Leave":
                        print("Ohkay! Your choice, you will find more pokemons during this journey")
                        time.sleep(2)
                        print("You started walking again towards the town.....")
                        time.sleep(2)
                        print("BOOM!! a wild Ninetails appeared")
                        time.sleep(2)
                        ae=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                        if ae=="Catch":
                            print("Solve this calculation to catch 'Ninetails' ")
                            af = int(input("12+685-43*45//3+12 : "))

                            if af==66:
                                print("GOTCHA!! You caught Ninetails ")
                                time.sleep(2)
                                print("Your Pokemon count increases by 1")
                                time.sleep(2)
                                print("Pokemon Count : 2")
                                time.sleep(2)
                                print("You started walking again towards the town.....")
                                time.sleep(2)
                                print("BOOM!! a wild Dragonite appeared")
                                time.sleep(2)
                                ae=input("Do you want to catch the pokemon or  leave the pokemon(Catch/Leave)")
                                if ae=="Catch":
                                    print("Arrange these jumbled words to catch 'Dragonite' ")
                                    af = input(" Y , O , T , N , H , P : ")
                                    if af=="PYTHON":
                                        print("GOTCHA!! You caught Dragonite ")
                                        time.sleep(2)
                                        print("Your Pokemon count increases by 1")
                                        time.sleep(2)
                                        print("Pokemon Count : 3")
                                        time.sleep(2)
                                        print("Now you entered the town. You met max and he challenges you for a pokemon battle,You accepted it")
                                        time.sleep(2)
                                        print("Max -->  You can't defeat me even you have 10 pokemons")
                                        time.sleep(2)
                                        print(b, " -->HAHAHA.... What a joke! Let's wait and watch who will win")
                                        time.sleep(2)
                                        print("You both started the battle ")
                                        time.sleep(2)
                                        print("Max has taken out the strongest among all...MEWTWO")
                                        time.sleep(2)
                                        print("Go Team",b, )
                                        print("Solve this riddle to win the battle")
                                        qr = input("I have lakes with no water, mountains with no stone, and cities with no buildings. What am I?")
                                        if qr == "Map":
                                            raj=input("Which attack do you want to do( Fearless Fire / Tornado )")
                                            if raj=="Fearless Fire":
                                                print("WOW!!! This attack was Super effective , Mewtwo fainted")

                                                print("Victory belongs to you ^_^")

                                                print(" ")
                                                print("Restart to play again :) ")

                                                print(" ")
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()
                                            elif raj=="Tornado":
                                                print("OHH!! Your attack was weak (●__●) ")

                                                print("Mewtwo attacked your team and your team fainted")

                                                print("You lose")

                                                print("Play again to take revenge")

                                                print(" ")
                                                print("Restart to play again :) ")

                                                print(" ")
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()
                                            else:
                                                print("you chose a wrong option.Restart your game you fool")

                                                print(" ")
                                                print("Restart to play again :) ")

                                                print(" ")
                                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                                if re == "Yes":
                                                    print('''


                            ---------------------------------------------------------------------------------------------------------------------


                                                            ''')
                                                    game()
                                                else:
                                                    print("Okay! Your choice")
                                                    exit()

                                        else:
                                            print("Mewtwo attacked your team and your team fainted")

                                            print("You lose")

                                            print("Play again to take revenge")

                                            print(" ")
                                            print("Restart to play again :) ")

                                            print(" ")
                                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                            if re == "Yes":
                                                print('''


                        ---------------------------------------------------------------------------------------------------------------------


                                                        ''')
                                                game()
                                            else:
                                                print("Okay! Your choice")
                                                exit()


                                    else:
                                        print("Dragonite disliked you.He attacked on you.You fainted")

                                        print("OHHH😩 You lost your game :( ")

                                        print("Restart your game to play again")

                                        print(" ")
                                        print("Restart to play again :) ")

                                        print(" ")
                                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                        if re == "Yes":
                                            print('''


                    ---------------------------------------------------------------------------------------------------------------------


                                                    ''')
                                            game()
                                        else:
                                            print("Okay! Your choice")
                                            exit()
                                elif ae=="Leave":
                                    print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")

                                    print("So you lost the game :( Restart the game to play again")

                                    print(" ")
                                    print("Restart to play again :) ")

                                    print(" ")
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()
                                else:
                                    print("you chose a wrong option.'YOU LOST' Restart your game you fool")

                                    print(" ")
                                    print("Restart to play again :) ")

                                    print(" ")
                                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                    if re == "Yes":
                                        print('''


                ---------------------------------------------------------------------------------------------------------------------


                                                ''')
                                        game()
                                    else:
                                        print("Okay! Your choice")
                                        exit()

                            else:
                                print("Ninetails disliked you.He attacked on you.You fainted")

                                print("OHHH😩 You lost your game :( ")
                                print("Restart your game to play again")

                                print(" ")
                                print("Restart to play again :) ")
                                print(" ")
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()




                        elif ae=="Leave":
                                print("To defeat MAX you should have atleast  3 pokemons which you can't have now.")

                                print("So you lost the game :( Restart the game to play again")

                                print(" ")
                                print("Restart to play again :) ")

                                print(" ")
                                re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                                if re == "Yes":
                                    print('''


            ---------------------------------------------------------------------------------------------------------------------


                                            ''')
                                    game()
                                else:
                                    print("Okay! Your choice")
                                    exit()

                        else:
                            print("you chose a wrong option.'YOU LOST' Restart your game you fool")

                            print(" ")
                            print("Restart to play again :) ")

                            print(" ")
                            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                            if re == "Yes":
                                print('''


        ---------------------------------------------------------------------------------------------------------------------


                                        ''')
                                game()
                            else:
                                print("Okay! Your choice")
                                exit()


                    else:
                        print("you chose a wrong option.'YOU LOST' Restart your game you fool")

                        print(" ")
                        print("Restart to play again :) ")

                        print(" ")
                        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                        if re == "Yes":
                            print('''


    ---------------------------------------------------------------------------------------------------------------------


                                    ''')
                            game()
                        else:
                            print("Okay! Your choice")
                            exit()
                else:
                    print("you chose a wrong option.Restart your game you fool")

                    print(" ")
                    print("Restart to play again :) ")

                    print(" ")
                    re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
                    if re == "Yes":
                        print('''


    ---------------------------------------------------------------------------------------------------------------------


                                ''')
                        game()
                    else:
                        print("Okay! Your choice")
                        exit()


        else:
            print("you chose a wrong option.Restart your game you fool")

            print(" ")
            print("Restart to play again :) ")

            print(" ")
            re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
            if re == "Yes":
                print('''


    ---------------------------------------------------------------------------------------------------------------------


                        ''')
                game()
            else:
                print("Okay! Your choice")
                exit()


    elif a=="No":
        print("Ohhh! So, You don't want some time to enjoy out of your boring life.Your Bad")
        time.sleep(2)
        print(" ")
        print("Restart to play again :) ")
        time.sleep(2)
        print(" ")
        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
        if re == "Yes":
            print('''


---------------------------------------------------------------------------------------------------------------------


                    ''')
            game()
        else:
            print("Okay! Your choice")
            exit()

    else:
        print("you chose a wrong option.Restart your game you fool")      
        print(" ")
        print("Restart to play again :) ")
        print(" ")
        re = input("Do you wanna Restart?(Write 'Yes' to play again) : ")
        if re == "Yes":
            print('''


    ---------------------------------------------------------------------------------------------------------------------



                    ''')
            game()
        else:
            print("Okay! Your choice")
            exit()

game()




                
    
    
                        


# In[ ]:





# In[ ]:




