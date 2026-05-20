import random

def show_menu():
    print("\n=== CODEQUEST ===")
    print("1. Start Game")
    print("2. Instructions")
    print("3. Exit")

def instructions():
    print("\nWelcome to CodeQuest!")
    print("Solve programming challenges to earn XP.")
    print("Correct answer = 10 XP")
    print("Try to complete all levels.\n")

def play_game():
    score = 0

    questions = [
        {
            "question": "Which keyword is used to define a function in Python?",
            "answer": "def"
        },
        {
            "question": "Which data type stores text?",
            "answer": "string"
        },
        {
            "question": "Which symbol starts a comment in Python?",
            "answer": "#"
        },
        {
            "question": "Which loop repeats while a condition is true?",
            "answer": "while"
        },
        {
            "question": "Which keyword is used for decision making?",
            "answer": "if"
        }
    ]

    random.shuffle(questions)

    for level, q in enumerate(questions, start=1):
        print(f"\nLevel {level}")
        user_answer = input(q["question"] + " ")

        if user_answer.lower() == q["answer"]:
            print("Correct! +10 XP")
            score += 10
        else:
            print("Wrong! Correct answer:", q["answer"])

    print("\nGame Finished!")
    print("Total XP:", score)

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
        print("Invalid option")