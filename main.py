import random

word_list = ["apple", "mango", "orange", "banana", "grapes", "pineapple", "papaya"]
chosen_word = random.choice(word_list)


stages = [
    """
   +---+
       |
       |
       |
      ===
""",
    """
   +---+
   O   |
       |
       |
      ===
""",
    """
   +---+
   O   |
   |   |
       |
      ===
 """,
    """
   +---+
   O   |
  \|   |
       |
      ===
 """,
    """
   +---+
   O   |
  \|/  |
       |
      ===
 """,
    """
   +---+
   O   |
  \|/  |
  /    |
      ===
 """,
    """
   +---+
   O   |
  \|/  |
  / \   |
      ===
 """,
]


display = []

for letter in chosen_word:
    display += "_"
print(display)

game_over = False
lives = 6

while not game_over:
    guessed_letter = input("Guess a letter : ").lower()
    flag = False

    for i in range(len(chosen_word)):
        if chosen_word[i] == guessed_letter:
            flag = True
            display[i] = guessed_letter
            print("Match")
            print(display)
            print(stages[6 - lives])
            print(f"You have still {lives} lives left")

    if "_" not in display:
        print("You won")
        break

    if flag == False:
        print("No Match")
        lives = lives - 1
        print(stages[6 - lives])
        if lives > 0:
            print(f"You have still {lives} lives left")

    if lives == 0:
        print("You lose. The man hanged and died")
        print(f"The word is {chosen_word}")
        break