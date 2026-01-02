# 1 for snake
# 0 for gun
# -1 for water
import random

computer = random.choice([1 , -1 , 0])
you = (input("what do you want to choose"))
yourstr = {"snake" : 1 , "gun" : 0 , "water" : -1}
yours = yourstr[you]
print(f"computer chose {computer} and you chose {yours[yourstr]}")
if( computer == yours):
     print("it is a draw")
elif (computer == 1 and yours == 0):
    print("you win")
elif (computer == 0 and yours == -1):
     print("you win")
elif (computer == -1 and yours == 1):
     print("you win")
elif (computer == 0 and yours == 1):
     print("computer wins")
elif (computer == 1 and yours == -1):
     print("computer wins")
elif (computer == -1 and yours == 0):
     print("computer wins") 
else:
     print("something went wrong")
