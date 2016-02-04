import random
with open("/usr/share/dict/words") as my_file:
    contents = my_file.read().splitlines()
random_word = random.choice(contents)
word = "ball"
num_of_tries = 8

empty_word = list("_" * len(random_word))
x = len(random_word)
print(empty_word)
print("Your game contains " + str(x) + " amount of letters, good luck!")

while num_of_tries > 0:

    if "_" not in empty_word:
        print("You are the WINNER!")
        break

    counter = 0
    guess = input("What is your guess? ")

    for character in random_word:

        if character == guess:
            empty_word[counter] = guess

        counter += 1

    if guess not in random_word:
        print("Wrong, try again!")
        num_of_tries -= 1
        print(str(num_of_tries) + " Guess(es) Remaining.")

    print(empty_word)
print("Your word was: " + str(random_word))