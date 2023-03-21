import random
print("this is my first project")
def get_choices():
    player_choice = input("enter a choice(rock, paper, scissors):")
    computer_options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(computer_options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices
def check_win(player, computer):
    print(f"you choose {player}, computer choose {computer}")
    if player == computer:
        return ("it's a tie")
    elif player == "rock":
        if computer == "scissors":
            return "rock smaches scissors you win"
        else: 
            return ("paper covers rock you lose")
    elif player == "paper":
        if computer == "rock":
            return ("paper covers rock you win")
        else: 
            return ("scissor cut paper you lose")
    elif player == "scissors":
        if computer == "paper":
            return ("scissors cut paper")
        else: 
            return ("rock smaches paper you lose")
        
choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
    
    

    
    

