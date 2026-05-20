import random

def show_menu():
    print("\n=== CODEQUEST ===")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Exit")

def instructions():
    print("\nWelcome to CodeQuest!")
    print("Answer programming questions to earn XP.")
    print("Each correct answer = 10 XP.")
    print("You have 3 lives. If you lose all lives, the game ends.\n")

def play_game():
    xp = 0
    lives = 3

    questions = [
        {"question": "Which keyword is used to define a function in Python?", "answer": "def"},
        {"question": "Which data type stores text?", "answer": "string"},
        {"question": "Which symbol starts a comment in Python?", "answer": "#"},
        {"question": "Which loop repeats while a condition is true?", "answer": "while"},
        {"question": "Which keyword is used for decision making?", "answer": "if"},
        {"question": "Which function prints output to the screen?", "answer": "print"},
        {"question": "Which function gets input from the user?", "answer": "input"}
    ]

    random.shuffle(questions)

    for level, q in enumerate(questions, start=1):
        if lives == 0:
            break

        print(f"\nLevel {level}")
        print("Lives:", lives)
        answer = input(q["question"] + " ")

        if answer.lower() == q["answer"]:
            print("Correct! +10 XP")
            xp += 10
        else:
            print("Wrong! Correct answer:", q["answer"])
            lives -= 1

    print("\nGame Over!")
    print("Your XP:", xp)

    if xp >= 50:
        print("Rank: Coding Master")
    elif xp >= 30:
        print("Rank: Python Explorer")
    else:
        print("Rank: Beginner")

while True:
    show_menu()
    choice = input("Choose an option: ")

    if choice == "1":
        play_game()
    elif choice == "2":
        instructions()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")