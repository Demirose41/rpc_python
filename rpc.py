#print ("rock")
#print ("paper")
#print ("scissors")
#
#print ("Who is the first challenger :")
#player1 = input()
#print ("Who is the second challenger :")
#player2 = input()
#
#
#
#print(f"{player1} VS {player2}")
#
#
#if player1 == player2 :
#     print("please find a friend") 
#elif player1 == "Car":
#    print("CAAAAAAAAAR")
#else :
#    print("FIGHT")
#    print("FIGHT")




##############
##with conditionals and functions## 
##############

#def comparison (x , y):
#    if x == "scissors" and y == "paper" :
#        return "p1"
#    if x == "rock" and y == "scissors" :
#        return "p1"
#    if x == "paper" and y == "rock" :
#        return "p1"
#    if x == y :
#        print("its a tie")
#        exit()
#    else :
#        return "p2"
#
#print("who will be first")
#p1_name = input()
#print("who will be second")
#p2_name = input()
#
#print(f"{p1_name} enter your choice")
#p1_option = input()
#print(f"{p2_name} enter your choice")
#p2_option = input()
#
#
#
#
#print( f"{comparison(p1_option, p2_option)} is the winner")




##############
##with loops## 
##############




###### VARIABLE 

#score_limit  
#winner 

###### FUNCTIONS
import math



def compare (x,y):
    if x == "scissors" and y == "paper" :
        return "p1"
    if x == "rock" and y == "scissors" :
        return "p1"
    if x == "paper" and y == "rock" :
        return "p1"
    else :
        return "p2"


        


score_p1 = 0
score_p2 = 0
round = 0 


print("who will be first")
p1_name = input()
print("who will be second")
p2_name = input()
print("how many rounds?")
win_condition = int(input()) / 2 
print(f"{win_condition} win con")
while score_p2 < win_condition  or score_p1 < win_condition:
    print(score_p2)
    print(score_p1)
    print(round)
    print(win_condition)
    input()
    score_p2 +=1 
    score_p1 += 1
    round += 1

print("out")

