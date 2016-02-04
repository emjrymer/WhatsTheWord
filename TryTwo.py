guessed_letter = input("What is your guess? ")
word = "ball"
counter = 0
compared_letter = word[counter]
ghosted_word = list("_" * len(word))
new_word = [letter for letter in word if letter not in ghosted_word]
print(new_word)
if guessed_letter in new_word:
    print()
    ghosted_word = ghosted_word.replace("_", new_word[guessed_letter])