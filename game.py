import random


def get_user_choice():
    while True:
        user_choice = input(
            "Enter your choice (rock, paper, or scissors): ").strip().lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")


def get_computer_choice():
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    return computer_choice


def determine_winner(user_choice, computer_choice):
    if (user_choice == computer_choice):
        return "draw"
    elif (user_choice == 'rock' and not computer_choice == 'rock'):
        if (computer_choice == "paper"):
            return "computer"
        else:
            return "user"
    elif (user_choice == 'paper' and not computer_choice == 'paper'):
        if (computer_choice == "scissors"):
            return "computer"
        else:
            return "user"
    elif (user_choice == 'scissors' and not computer_choice == 'scissors'):
        if (computer_choice == "rock"):
            return "computer"
        else:
            return "user"


def update_score(winner, scores):
    if (winner == "user"):
        scores[winner] += 1
    elif (winner == "computer"):
        scores[winner] += 1
    elif (winner == "draw"):
        scores[winner] += 1


def display_score(scores):
    return print( f"User: {scores['user']} | Computer: {scores['computer']} | Draws: {scores['draw']}")


def play_again():
    while True:
        user_input = input("Do you want to continue? (yes/no): ").lower()

        if user_input == 'yes':
            return True
        elif user_input == 'no':
            return False
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")


def main():
    scores = {'user': 0, 'computer': 0, 'draw': 0}
    print("Welcome To Rock, Paper, Scissors Game!")

    while True:
        x = get_user_choice()
        y = get_computer_choice()
        print(f"computer_choice: {y}")
        
        winner = determine_winner(x, y)
        update_score(winner, scores)
        display_score(scores)
        
        if not play_again():
            break

    print("Thank you for playing Rock, Paper, Scissors!")


if __name__ == "__main__":
    main()
