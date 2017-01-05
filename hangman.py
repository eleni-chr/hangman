import re
import random

words = open("largewords.txt").read().splitlines()

random_word = random.choice(words)
lives = 6
letters_used = []
current_word = list(len(random_word)*"_")

while True:
    print("\nWord: ", end=' ')
    for ch in current_word:
        print(ch, end=' ')
    print("\n")
    print("Attempts left: " + str(lives) + ", " + " Letters used: " + str(letters_used))
    letter = input("\nType a letter: ")

    if len(letter) > 1:
        if letter == random_word:
            print("Congratulations! You won!")
        else:
            print("Wrong! You lost! The correct word is " + random_word)
        break

    letters_used.append(letter)

    found_letter = False
    for i, ch in enumerate(random_word):
        if ch == letter:
            found_letter = True
            current_word[i] = letter

    if not found_letter:
        lives -= 1
        print("\nThis letter is not in the word.\n")

    if lives == 0:
        print("You lost! The correct word is " + random_word)
        break

    if "_" not in current_word:
        print("\nWord: ", end=' ')
        for ch in current_word:
            print(ch, end=' ')
        print("\n\nCongratulations! You won!")
        break
