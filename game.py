import random
player_me=0
player_c=0
x=["papper","rock","scissors"]
player_1=random.choice(x)
player_2=str(input("play (papper,rock,scissors): "))
out=""
player_2=str(out)
while  out=="start":  
        out=input("enter start to play :")
        if player_1==player_2 :
            print("computer was choose : ", player_1)
            print("computer was choose your choice , play again")
            print("computer: ",player_c,"you: ", player_me)
            break
        elif player_1=="papper" and player_2=="rock":
            print("computer was choose :", player_1)
            print("lose!")
            player_c +=1
            print("computer: ",player_c,"you: ", player_me)

        elif player_1=="papper" and player_2=="scissors":
            print("computer was choose :", player_1)
            print("win!")
            player_me +=1
            print("computer: ",player_c,"you: ", player_me)

        elif player_1=="rock" and player_2=="papper":
            print("computer was choose :", player_1)
            print("win!")
            player_me +=1
            print("computer: ",player_c,"you: ", player_me)

        elif player_1=="rock" and player_2=="scissors":
            print("computer was choose :", player_1)
            print("lose!")
            player_c +=1
            print("computer: ",player_c,"you: ", player_me)

        elif player_1=="scissors" and player_2=="rock":
            print("computer was choose :", player_1)
            print("win!")
            player_me +=1
            print("computer: ",player_c,"you: ", player_me)

        elif player_1=="scissors" and player_2=="papper":
            print("computer was choose :", player_1)
            print("lose!")
            player_c +=1
            print("computer: ",player_c,"you: ", player_me)
        else:
            print("please choose (papper,rock,scissors):")                                       
            