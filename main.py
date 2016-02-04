word = "ball"
num_of_tries = 8

empty_word = list("_" * len(word))
print(empty_word)

while num_of_tries > 0:
    if "_" not in empty_word:
        print("You are the WINNER!")
        break
    counter = 0
    guess = input("What is your guess? ")
    for character in word:
        if character == guess:
            empty_word[counter] = guess
        counter += 1

    if guess not in word:
        print("Wrong, try again!")
        num_of_tries -= 1
        print(str(num_of_tries) + " Guess(es) Remaining.")



    print(empty_word)
