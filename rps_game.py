# rock, paper, scissors game
import random  # so the computer can pick a random choice


def get_choices():
    player_choice = input("Enter a choice ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    return choices


def check_win(player, computer):
    print(f"You chose {player}, computer chose {computer}")
    if player.casefold() == computer.casefold():
        return "It's a tie🤞"
    elif player.casefold() == "rock":
        if computer.casefold() == "scissors":
            return "YOU WIN🏆"
        else:
            return "YOU LOSE😭"
    elif player.casefold() == "scissors":
        if computer.casefold() == "paper":
            return "YOU WIN🏆"
        else:
            return "YOU LOSE😭"
    elif player.casefold() == "paper":
        if computer.casefold() == "rock":
            return "YOU WIN🏆"
        else:
            return "YOU LOSE😭"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
