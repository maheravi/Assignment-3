import random

items = ["Rock", "Paper", "Scissors"]
computer_score = 0
user_score = 0

print("0- Rock")
print("1- Paper")
print("2- Scissors")

user_choice_index = 0

while True:
    index = random.randint(0, 2)
    computer_choice = items[index]
    computer_choice = random.choice(items)
    user_choice_index = int(input())
    user_choice = items[user_choice_index]
    if computer_choice == "Rock" and user_choice == "Scissors":
        print("computer wins")
        computer_score += 1
    elif computer_choice == "Scissors" and user_choice == "Paper":
        print("computer wins")
        computer_score += 1
    elif computer_choice == "Paper" and user_choice == "Rock":
        print("computer wins")
        computer_score += 1
    elif computer_choice == user_choice:
        print("It's a tie!")
    else:
        print("You wins")
        user_score +=1
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
print('Your Score: ', user_score)
print('Computer Score: ', computer_score)
