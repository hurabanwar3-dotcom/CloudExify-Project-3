import random


question_bank = [
    {
        "text": "Which symbol is used to assign a value to a variable?",
        "choices": {
            "A": "==",
            "B": "=",
            "C": "!=",
            "D": ":="
        },
        "correct": "B"
    },

    {
        "text": "Which Python data type stores multiple values in an ordered collection?",
        "choices": {
            "A": "list",
            "B": "float",
            "C": "boolean",
            "D": "integer"
        },
        "correct": "A"
    },

    {
        "text": "Which keyword is used to create a loop that continues while a condition is true?",
        "choices": {
            "A": "repeat",
            "B": "loop",
            "C": "while",
            "D": "continue"
        },
        "correct": "C"
    },

    {
        "text": "Which function is commonly used to display information in Python?",
        "choices": {
            "A": "show()",
            "B": "display()",
            "C": "output()",
            "D": "print()"
        },
        "correct": "D"
    },

    {
        "text": "Which data type represents True or False?",
        "choices": {
            "A": "str",
            "B": "bool",
            "C": "int",
            "D": "float"
        },
        "correct": "B"
    },

    {
        "text": "Which brackets are normally used to create a Python list?",
        "choices": {
            "A": "()",
            "B": "{}",
            "C": "[]",
            "D": "<>"
        },
        "correct": "C"
    },

    {
        "text": "Which keyword is used when defining a function?",
        "choices": {
            "A": "func",
            "B": "define",
            "C": "def",
            "D": "function"
        },
        "correct": "C"
    },

    {
        "text": "Which function allows a Python program to receive input from the user?",
        "choices": {
            "A": "input()",
            "B": "read()",
            "C": "get()",
            "D": "scan()"
        },
        "correct": "A"
    },

    {
        "text": "What does len() generally return?",
        "choices": {
            "A": "The largest value",
            "B": "The number of items",
            "C": "The data type",
            "D": "The memory size"
        },
        "correct": "B"
    },

    {
        "text": "Which keyword is used to test another condition after if?",
        "choices": {
            "A": "otherwise",
            "B": "elseif",
            "C": "elif",
            "D": "then"
        },
        "correct": "C"
    },

    {
        "text": "Which method converts text into uppercase letters?",
        "choices": {
            "A": "upper()",
            "B": "uppercase()",
            "C": "capital()",
            "D": "up()"
        },
        "correct": "A"
    },

    {
        "text": "Which collection stores data using key and value pairs?",
        "choices": {
            "A": "list",
            "B": "tuple",
            "C": "dictionary",
            "D": "set"
        },
        "correct": "C"
    },

    {
        "text": "Which function is useful for generating a sequence of numbers?",
        "choices": {
            "A": "numbers()",
            "B": "range()",
            "C": "sequence()",
            "D": "count()"
        },
        "correct": "B"
    },

    {
        "text": "Which mode opens a file for writing?",
        "choices": {
            "A": "r",
            "B": "x",
            "C": "w",
            "D": "read"
        },
        "correct": "C"
    },

    {
        "text": "Which statement is used to exit a loop immediately?",
        "choices": {
            "A": "stop",
            "B": "exit",
            "C": "break",
            "D": "end"
        },
        "correct": "C"
    }
]

def run_question(question, number, total):
    print()
    print("=" * 45)
    print(f"Question {number} of {total}")
    print("=" * 45)
    print(question["text"])
    print()

    for key, value in question["choices"].items():
        print(f"{key}. {value}")

    while True:
        user_answer = input("\nEnter your answer: ").strip().upper()

        if user_answer in question["choices"]:
            break

        print("Invalid choice. Please enter A, B, C, or D.")

    if user_answer == question["correct"]:
        print("Correct! Nice job.")
        return True

    correct_option = question["correct"]
    correct_answer = question["choices"][correct_option]

    print(f"Incorrect. The correct answer is {correct_option}. {correct_answer}")
    return False
def calculate_result(score, total):
    percentage = (score / total) * 100

    if percentage >= 90:
        grade = "A"
    elif percentage >= 80:
        grade = "B"
    elif percentage >= 70:
        grade = "C"
    elif percentage >= 60:
        grade = "D"
    else:
        grade = "F"

    return percentage, grade
def load_high_score():
    try:
        with open("highscore.txt", "r") as file:
            data = file.read().strip()

        if data == "":
            return 0

        return int(data)

    except (FileNotFoundError, ValueError):
        return 0


def save_high_score(score):
    previous_score = load_high_score()

    if score > previous_score:
        with open("highscore.txt", "w") as file:
            file.write(str(score))

        print(f"New high score! You scored {score}.")
        return True

    return False
def start_quiz():
    available_questions = question_bank.copy()

    random.shuffle(available_questions)

    selected_questions = available_questions[:10]

    score = 0

    print()
    print("=" * 45)
    print("          PYTHON QUIZ CHALLENGE")
    print("=" * 45)
    print(f"You will answer {len(selected_questions)} questions.")
    print("Choose A, B, C, or D.")
    print("=" * 45)

    input("Press Enter when you are ready...")

    for number, question in enumerate(selected_questions, start=1):
        result = run_question(
            question,
            number,
            len(selected_questions)
        )

        if result:
            score += 1

        percentage, grade = calculate_result(
        score,
        len(selected_questions)
    )

    print()
    print("=" * 45)
    print("             QUIZ FINISHED")
    print("=" * 45)
    print(f"Score      : {score} / {len(selected_questions)}")
    print(f"Percentage : {percentage:.1f}%")
    print(f"Grade      : {grade}")
    print("=" * 45)

    save_high_score(score)


def main():
    while True:
        start_quiz()

        print()
        choice = input("Would you like to play again? (yes/no): ").strip().lower()

        if choice not in ["yes", "y"]:
            print()
            print("Thanks for playing the Python Quiz Challenge!")
            print("Goodbye!")
            break


main()