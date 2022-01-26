
secret_word = "Jes"
guess = ""
guess_count = 0
guess_limit = 10
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < 2:
        guess = input ("Enter guess: ")
        guess_count += 1
    elif guess_count == 2 and guess_count < guess_limit:
        print("It's a three letter word")
        guess = input("Enter guess: ")
        guess_count += 1
    elif guess_count == 4 and guess_count < guess_limit:
        print("They're a really cute gamer")
        guess = input("Enter guess: ")
        guess_count += 1
    elif guess_count == 6 and guess_count < guess_limit:
        print("They have several annoying and amazing pets")
        guess = input("Enter guess: ")
        guess_count += 1
    elif guess_count == 8 and guess_count < guess_limit:
        print("Two more chances, silly")
        guess = input("Enter guess: ")
        guess_count += 1
    elif guess_count < guess_limit:
        guess = input ("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True


if out_of_guesses:
    print("Out of Guesses, please try again!")
else:
    print("You truly are the best person in the world, thank you for picking me! I love you so so much!")