import random
def get_user_choice():
    user_choice = input("Enter your choice (rock,paper,scissors);").lower()
    if user_choice not in ["rock","paper","scissos"]:
        print("Invalid choice.please try again.")
        return get_user_choice()
    return user_choice
def get_computer_choice():
    return random.choice(["rock","paper","scissors"])
def determine_winner(user_choice,computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif(user_choice == "rock" and computer_choice == "scissors")or \
                     (user_choice == "paper" and computer_choice == "rock")or \
                     (user_choice == "scissors" and computer_choice == "paper"):
        return "you win!"
    else:
        return "computer wins!"
def play_game():
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f"you chose:{user_choice}")
    print(f"computer chose:{computer_choice}")
    print(determine_winner(user_choice,computer_choice))
if __name__ == "__main__":
    play_game()
