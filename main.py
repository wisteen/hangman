from hangman import stages, logo
from words import word_list
import random
print(logo)
chosen_word = random.choice(word_list).lower()
playing = True
board = []
life = 6
for _ in chosen_word:
        board += "_"

print(board)
while playing:

    chosen_letter = input("Guess a letter:    ").lower()

    position = 0
    for letters in chosen_word:

        if chosen_letter == letters:
            board[position] = letters
        position += 1


    if chosen_letter not in chosen_word:
            print("lost a life")
            life -= 1
            print(stages[life])

    if life == 0:
            print("GAME OVER")
            playing = False
    if "_" not in board:
            print("YOU ARE THE WINNER")
            playing = False


    print(board)
