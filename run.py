"""
Collection for the questions
"""
questions = {
    "Which is the biggest planet in our solar system?: ": "A",
    "Which is the biggest mammal on planet earth?: ": "B",
    "Which is the fastest animal on planet earth?: ": "A",
    "Who wrote the epic stories of Harry Potter?: ": "C",
    "Who wrote the famous book The Alchemist?: ": "D",
    "What's The Batman's real name?: ": "D",
    "What's the name of the director of The Gladiator starring Russell Crowe?: ": "A",
    "How many letters are there in the English alphabet?: ": "B",
    "Who made the Mona Lisa painting?: ": "A",
    "How many bones does the human hand have?: ": "A",
}

"""
Collection for the options
"""
options = [
    ["A. Jupiter", "B. Uranus", "C. Saturn", "D. Neptune"],
    ["A. Elephant", "B. Blue Whale", "C. Gray Whale", "D. Clown Fish"],
    ["A. Peregrine Falcon", "B. Cheetah", "C. Black Marlin", "D. Turtle"],
    ["A. J.R.R. Tolkien", "B. Stephen King", "C. J.K. Rowling", "D. George Orwell"],
    ["A. Ian Fleming", "B. William Shakespeare", "C. C.S. Lewis", "D. Paulo Coelho"],
    ["A. Clark Kent", "B. Peter Parker", "C. Chuck Norris", "D. Bruce Wayne"],
    ["A. Ridley Scott", "B. Martin Scorsese", "C. Christopher Nolan", "D. Guillermo del Toro"],
    ["A. 25", "B. 26", "C. 27", "D. 28"],
    ["A. Vincent van Gogh", "B. Leonardo da Vinci", "C. Pablo Picasso", "D. Claude Monet"],
    ["A. 27", "B. 26", "C. 25", "D. 30"],
]

"""
Function for new game
"""

def new_game():
    print("-------------------------")
    print("WELCOME TO MY QUIZGAME!")
    guesses = []
    correct_guesses = 0
    question_number = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_number - 1]:
            print(i)
        guess = input("Enter (A, B, C, D):\n ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_number += 1

    display_score(correct_guesses, guesses)

"""
Function to check the answers
"""
def check_answer(answer, guess):
    if answer == guess:
        print("Correct answer!")
        return 1
    else:
        print("Wrong answer!")
        return 0

"""
Function to display the score
"""
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("Results")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses / len(questions)) * 100)
    print("Your Score is: " + str(score) + "%")

"""
Function to replay the game
"""
def play_again():
    response = input("Play again? (Yes or No):\n ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False


new_game()
while play_again():
    new_game()

print("SEE YOU SOON")
