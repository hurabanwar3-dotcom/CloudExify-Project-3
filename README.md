# Python Quiz Game

## Description

The Python Quiz Game is a Python console application that tests the user's knowledge of basic Python programming concepts. The game randomly selects 10 questions from a question bank and presents four multiple choice options for each question. The system checks the user's answers, calculates the score, percentage, and grade, and saves the highest score for future games.

## Features Implemented

• Randomly select questions from the question bank
• Display 10 questions per game
• Multiple choice questions with four options
• Validate user answers
• Calculate total score
• Calculate percentage
• Assign grades based on performance
• Save and load high score
• Display previous high score
• Play the game again
• Exit with a goodbye message

## Technologies Used

• Python 3
• Random Module
• File Handling
• Lists
• Dictionaries
• Functions
• Loops
• Conditional Statements

## Project Structure

CloudExify_Project_3/
│
├── quiz_game.py
├── highscore.txt
├── README.md
│
└── Screenshots/
    ├── menu.png
    ├── question.png
    ├── result.png
    └── high_score.png
```

## Requirements

• Python 3.x

## How to Run

1. Clone or download this repository.
2. Open the project folder in VS Code or any Python IDE.
3. Open the terminal.
4. Run the following command:

python quiz_game.py


5. Press Enter to start the quiz.
6. Enter A, B, C, or D for each question.
7. Complete all 10 questions.
8. View your score, percentage, and grade.
9. Choose whether to play again.

## How the Game Works

The game contains a question bank with multiple Python programming questions. Before each game, the questions are shuffled and 10 questions are selected randomly.

For each question, the user selects one of four options. The answer is checked immediately and the score is updated when the answer is correct.

After completing all 10 questions, the game displays the total score, percentage, and grade.

## High Score System

The highest score is stored in the `highscore.txt` file.

When the player achieves a score higher than the previous high score, the file is automatically updated with the new score.

The saved high score is displayed when a new game starts.


## Challenges Faced

• Managing Python indentation correctly.
• Implementing random question selection.
• Validating user input.
• Calculating percentage and grades correctly.
• Reading and writing the high score using a text file.
• Organizing multiple functions into one application.

## How I Solved Them

• Used consistent 4 space indentation throughout the project.
• Used Python's `random` module to shuffle the question bank.
• Added input validation to accept only A, B, C, or D.
• Created a separate function to calculate the percentage and grade.
• Used file handling to save and load the high score.
• Divided the program into separate functions for better organization.

## Future Improvements

If given more time, I would like to add:

• Timer for each question
• Different difficulty levels
• Question categories
• Player name and leaderboard
• More questions
• Graphical User Interface (GUI)
• Database integration

## Author

**Hurab Anwar**

**Registration Number:** CX-INT-2026-PY-0054
