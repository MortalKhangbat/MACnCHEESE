secret_word = "weeb"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Secret Word Guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if guess == secret_word:
    print("Guees u a weeb gottem lmao!")
else:
    print("You BIG Loser out of guesses!!")


