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
    if x == y :
        return "tie"
    else :
        return "p2"


def divider () :
    for num in range (0,24,2) :
        print("####################################\n")
        print("# # # # # # # # # # # # # # # # # #\n")

def hud () :
    print(f"SCORE \n {score_p1} - {score_p2}")
    print(f"Round {round}")

def prompt(x) :
    print("####################################\n") 
    print(f"{x}! WHAT IS YOUR CHOICE")
    print("\n####################################\n\n")
    return input()

def reset() :
    global score_p1 
    global score_p2 
    global round   
    score_p1 = 0
    score_p2 = 0
    round    = 0



score_p1 = 0
score_p2 = 0
round = 0 
volition = True
live_score = {score_p1,score_p2}


while volition == True :
    divider()
    print("who will be first")
    p1_name = input()
    print("who will be second")
    p2_name = input()
    win_condition = math.ceil( int(input("Best of :")) / 2 )
    while score_p2 < win_condition  and score_p1 < win_condition :
        hud()
        p1_input = prompt(p1_name)
        divider()
        p2_input = prompt(p2_name)

        outcome = compare(p1_input,p2_input)

        if outcome == "p1" :
            score_p1 += 1 
            round += 1
            divider()
            print(f"{p1_name} is the winner of this round")
            input("continue")
            divider()
        elif outcome == "p2" :
                score_p2 += 1
                round += 1
                divider()
                print(f"{p2_name} is the winner of this round")
                input("continue")
                divider()
        else :
            divider()
            print("Tie ")
            input("continue")
            divider()
            
    hud()
    rematch = input("wanna play again?\n y/n :") 
    if rematch.lower() == "y" :
        reset()
        divider()
    else :
        print(":¨·.·¨: \n `·. ƮϦαɳk Ψөu For Playing")
        input()
        volition = False

