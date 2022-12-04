from random import randint

rand = randint(1, 100)

print("**** WELCOME GUESS THE NUMBER GAME ****")

guess = False


def guess_game():
    global guess
    while not guess:
        userinput = int(input("Your Guess Between 1 and 100: "))

        if userinput == rand:
            guess = True
            print("******** Well Done, You Won ********")

        elif userinput <= 0:
            print("Please enter between 1-100")

        elif userinput >= 101:
            print("Please enter between 1-100")

        elif userinput < rand:
            print("Too Low please enter little bit higher")

        elif userinput > rand:
            print("Too high please enter little bit lower")

        else:
            print("Something if Wrong")


guess_game()
