import random
from enum import IntEnum

class Action(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2

victories = {
    Action.Rock: [Action.Scissors], #Rock beats scissors
    Action.Paper: [Action.Rock], #Paper beats rock
    Action.Scissors: [Action.Paper] #Scissors beats paper
}

#user action
def get_user_selection():

    #user_action = input("Enter a choice (rock[0], paper[1], scissors[2]): ")
    choices = [f"{action.name}[{action.value}]" for action in Action]
    choices_str = ", ".join(choices)
    selection = int(input(f"Enter a choice ({choices_str}): "))
    action = Action(selection)
    return action

#computers action
def get_computer_selection():
    selection = random.randint(0, len(Action) - 1)
    action = Action(selection)
    return action

#dtermine who won the game
def winner(user_action, computer_action):

    defeats = victories[user_action]
    if user_action == computer_action:
        print(f"Both players selected {user_action.name}. The game is tied/drawn")

    elif computer_action in defeats:
        print(f"{user_action.name} beats {computer_action.name}! You won the game.")

    else:
        print(f"{computer_action.name} beats {user_action.name}! You lose the game.")

        
#main loop
while True:
    try:
        user_action = get_user_selection()

    except ValueError as e:
        range_str = f"[0, {len(Action) - 1}] "
        print(f"Invalid selection. Enter a value in range {range_str}")
        continue
    computer_action = get_computer_selection()
    winner(user_action, computer_action)

    player_again = input("Play the game again?(y/n):")
    if player_again.lower() != "y":
        break




