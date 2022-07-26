import random


def guess(number):
    random_num = random.randint(1, number)
    # we don't want user_input to equal random number off the bat so something outside the range
    user_input = 0
    while random_num != user_input:
        user_input = int(input(f"Guess a number between 1 and {number}: "))
        if random_num < user_input:
            print("That is too high!~")
        elif random_num > user_input:
            print("That is too low!~")
    print("You Win that was right!!!")

# guess(20)


def CPUguess(number):
    low = 1
    high = number
    feedback = ""
    while feedback != "c":
        compguess = random.randint(low, high)
        feedback = input(f"is {compguess}, Too high (h), Too low (l), Correct(c)?: ").lower()
        if feedback == "h":
            high = compguess - 1
        elif feedback == "l":
            low = compguess + 1
    print(f"Yep {compguess} the number!")

# CPUguess(100)

# this rps game can be improved


def rps():
    compscore = 0
    userscore = 0
    userchoice = 0
    while userchoice != "q":
        compchoice = random.choice(["Rock", "Paper", "Scissor"]).lower()
        userchoice = input("Rock, Paper, Scissor, or q to Quit?: ").lower()
        print(f"The Computer picked {compchoice}!")
        if compchoice == "rock" and userchoice == "scissor":
            compscore += 1
        elif compchoice == "paper" and userchoice == "rock":
            compscore += 1
        elif compchoice == "scissor" and userchoice == "paper":
            compscore += 1
        elif compchoice == userchoice:
            compscore += 0
        else:
            userscore += 1
    print(f"The cpu won {compscore} times & You won {userscore} times")
    print("Thanks for playing")

# rps()







