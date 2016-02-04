
word = "ball"
num_of_tries = 8

##list of letters and their corresponding position in the word
#listed_word = list(enumerate(word))
##prints letters in word
#for l in listed_word:
#    print(l[0])

empty_word = list("_" * len(word))
print(empty_word)

while num_of_tries > 0:
    counter = 0
    guess = input("What is your guess? ")
    for character in word:
        if character == guess:
            empty_word[counter] = guess
            #print(counter)
        counter += 1
    else:
        print("Wrong, try again!")
        num_of_tries -= 1
        print(str(num_of_tries) + " Guess(es) Remaining.")

    print(empty_word)












##prints word with guess as "_" :(
'''letters = list(l[1])
if guess in letters:
    word = (word.replace("_", "guess").replace(" ", "_ "))
    print(word)

def lett_pos(l):
    return l[0]

print(lett_pos(listed_word))'''