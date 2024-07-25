from random import randint
#from art import logo
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#function to check the user's guess against actual answer

def check_answer(guess , answer , turns):
    """ checks answer against guess. Returns the number of turns remaining"""
    if guess> answer:
        print("Too high ")
        return turns - 1
    elif guess < answer:
        print("Too low")
        return turns - 1
    else:
        print(f"You get the right answer that's{answer}")

    #Mkae function to set difficulty/
def set_difficulty():
    level = input("choose a difficulty .Type 'easy' or 'Hard'")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    #choosing a random number between  to 100
    print("Welcome to the number guessing game !")
    print("I'm thinking of a number between 1 and 100")
    answer= randint(1,100)

    turns = set_difficulty()
    guess=0
    while guess != answer:
        print(f"you have {turns} attempt remaining to guess the number")

        #let the user guess a number.
        guess = int(input("Make a guess : "))

        turns = check_answer(guess,answer,turns)
        if turns == 0:
            print ("You have  run out of guess , you loose ")
            return
        elif guess!= answer:
            print("Guess again.")

game()