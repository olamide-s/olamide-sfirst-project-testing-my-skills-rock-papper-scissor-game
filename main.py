import random
print("this is my first project")

choose_no_of_time_to_play = int(input("how many time do you want to play"))
def get_choices():
    player_choice = input("enter a choice(rock, paper, scissors):")
    computer_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
def check_win(player, computer):
    score = 0
    print(score)

    print(f"you choose {player}, computer choose {computer}")
    if player == computer:
        return ("it's a tie")
    elif player == "rock":
        if computer == "scissors":
            score += 1
            return ("rock smaches scissors you win")
        else: 
            return ("paper covers rock you lose")
    elif player == "paper":
        if computer == "rock":
            score += 1
            return ("paper covers rock you win")
        else: 
            return ("scissor cut paper you lose")
    elif player == "scissors":
        if computer == "paper":
            score += 1
            return ("scissors cut paper you win")
        else: 
            return ("rock smaches paper you lose")
    print(score)
        
#def record_score(choose_no_of_time_to_play):
# score = 0
#
# if result == "it's a tie":
#     print(score)
#     return "+0 point"
# 
# elif result == "paper covers rock you win":
#     
#     score += 1
#     print(score)
#     return "+1 point"
# 
# elif result == "rock smaches scissors you win":
#     
#     score += 1
#     print(score)
#     return "+1 point"
# 
# elif result == "scissors cut paper you win":
#     
#     score += 1
#     print(score)
#     return "+1 point"
# 
# elif result == "paper covers rock you lose":
#     print(score)
#     return "+0 point"
# 
# elif result == "scissor cut paper you lose":
#     print(score)
#     return "+0 point"
# 
# elif result == "rock smaches paper you lose":
#                 print(score)5
#
#                 return "+0 point"
        
                




number_of_time_played = choose_no_of_time_to_play 
i = 0
while i < number_of_time_played:
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    print(result)
    i += 1


    
    

    
    

