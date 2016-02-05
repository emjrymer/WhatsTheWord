import random
import sys
import math

def infinity():
    z = math.inf
    return z

def start():
    level = input("Do you want to play easy, medium, or hard? E, M, H?  ")
    if level.lower() == "e":
        random_word = pick_word(4, 6)
        return game(random_word)
    elif level.lower() == "m":
        random_word = pick_word(6, 10)
        return game(random_word)
    elif level.lower() == "h":
        random_word == pick_word(10, infinity())
        return game(random_word)

def pick_word(min_letter, max_letter):
    with open("/usr/share/dict/words") as my_file:
        contents = my_file.read().splitlines()
    the_cool = [word.lower() for word in contents if min_letter <= word <= max_letter]
    random_word = random.choice(the_cool)
    return random_word

def game(random_word):

    num_of_tries = 8
    empty_word = list("_" * len(random_word))
    x = len(random_word)

    while True:
        print(empty_word)
        print("Your game contains " + str(x) + " amount of letters, good luck!")
        d = []
        while num_of_tries > 0:
            print("Poor guesses: " + str(d))
            if "_" not in empty_word:
                #create function
                print("You are the WINNER!")
                break

            counter = 0
            guess = input("What is your guess? ")

            for character in random_word:

                if character == guess:
                    empty_word[counter] = guess

                counter += 1

            if guess not in random_word:
               #look at creating a function instead
                d.append(guess)
                print("Wrong, try again!")
                num_of_tries -= 1
                print(str(num_of_tries) + " Guess(es) Remaining.")

            print(empty_word)

        print("Your word was: " + str(random_word))
        play_again()

def play_again():
    answer = input("Would you like to play again? Y/N ")
    if answer.lower() == "n":
        sys.exit()
    elif answer.lower() == "y":
        game()
start()