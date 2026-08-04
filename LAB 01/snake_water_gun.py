# ==========================================================
# Python Lab Assignment
# Project : Snake Water Gun Game
# Developed By : Engr. Muhammad Javed
# ==========================================================

import random

# ==========================================================
# Task 1 : Introduction
# ==========================================================

print("=" * 60)
print("            WELCOME TO SNAKE WATER GUN GAME")
print("=" * 60)

player_name = input("Enter Your Name : ")

print(f"\nWelcome {player_name}! Best of Luck.\n")

# ==========================================================
# Task 2 : Variables
# ==========================================================

player_score = 0
computer_score = 0
draw_score = 0
total_matches = 0

# ==========================================================
# Task 3 : Dictionary
# ==========================================================

player = {
    "Name": player_name,
    "Wins": 0,
    "Losses": 0,
    "Draws": 0
}

# Used to convert user input into numbers
choice_dict = {
    "s": 1,
    "w": -1,
    "g": 0
}

# Used to display names
reverse_dict = {
    1: "Snake",
    -1: "Water",
    0: "Gun"
}

# ==========================================================
# Task 4 : List
# ==========================================================

history = []

# ==========================================================
# Task 5 : Tuple
# ==========================================================

rules = (
    "Snake drinks Water",
    "Water damages Gun",
    "Gun kills Snake"
)

# ==========================================================
# Task 6 : Main Program (While Loop)
# ==========================================================

while True:

    print("\n" + "=" * 60)
    print("                  MAIN MENU")
    print("=" * 60)
    print("1. Play Game")
    print("2. Show Rules")
    print("3. Show Score")
    print("4. Match History")
    print("5. Exit")

    menu = input("\nEnter Your Choice : ")

    # ======================================================
    # Play Game
    # ======================================================

    if menu == "1":

        print("\nChoose Your Move")
        print("s = Snake")
        print("w = Water")
        print("g = Gun")

        you_str = input("\nEnter Your Choice : ").lower()

        if you_str not in choice_dict:
            print("\nInvalid Choice! Please Enter s, w or g.")
            continue

        computer = random.choice([1, -1, 0])
        you = choice_dict[you_str]

        print("\n------------------------------")
        print(f"You Chose      : {reverse_dict[you]}")
        print(f"Computer Chose : {reverse_dict[computer]}")
        print("------------------------------")

        total_matches += 1

        # Draw
        if computer == you:

            print("\nMatch Draw!")

            draw_score += 1
            player["Draws"] += 1

            history.append(
                f"{reverse_dict[you]} vs {reverse_dict[computer]} --> Draw"
            )

        else:

            # Player Wins
            if (computer == -1 and you == 1) or \
               (computer == 1 and you == 0) or \
               (computer == 0 and you == -1):

                print("\nCongratulations! You Win.")

                player_score += 1
                player["Wins"] += 1

                history.append(
                    f"{reverse_dict[you]} vs {reverse_dict[computer]} --> Win"
                )

            # Computer Wins
            else:

                print("\nComputer Wins!")

                computer_score += 1
                player["Losses"] += 1

                history.append(
                    f"{reverse_dict[you]} vs {reverse_dict[computer]} --> Lose"
                )

    # ======================================================
    # Show Rules
    # ======================================================

    elif menu == "2":

        print("\n" + "=" * 60)
        print("                    GAME RULES")
        print("=" * 60)

        # Task : For Loop
        for i in range(len(rules)):
            print(f"{i + 1}. {rules[i]}")

        print("=" * 60)

    # ======================================================
    # Show Score
    # ======================================================

    elif menu == "3":

        print("\n" + "=" * 60)
        print("                 SCORE BOARD")
        print("=" * 60)

        print(f"Player Name   : {player['Name']}")
        print(f"Wins          : {player['Wins']}")
        print(f"Losses        : {player['Losses']}")
        print(f"Draws         : {player['Draws']}")
        print(f"Total Matches : {total_matches}")

        print("=" * 60)

    # ======================================================
    # Match History
    # ======================================================

    elif menu == "4":

        print("\n" + "=" * 60)
        print("                 MATCH HISTORY")
        print("=" * 60)

        if len(history) == 0:
            print("No Match Played Yet!")

        else:

            # Task : For Loop
            for i in range(len(history)):
                print(f"{i + 1}. {history[i]}")

        print("=" * 60)

    # ======================================================
    # Exit
    # ======================================================

    elif menu == "5":

        print("\n" + "=" * 60)
        print("           THANK YOU FOR PLAYING")
        print("=" * 60)

        print(f"Player Name   : {player['Name']}")
        print(f"Total Matches : {total_matches}")
        print(f"Wins          : {player['Wins']}")
        print(f"Losses        : {player['Losses']}")
        print(f"Draws         : {player['Draws']}")

        print("\nDeveloped By : Engr. Muhammad Javed")
        print("=" * 60)

        break

    # ======================================================
    # Invalid Menu
    # ======================================================

    else:
        print("\nInvalid Menu Choice! Please Try Again.")