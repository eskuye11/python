import random


msg = """\n I am thinking a number between '1' and '100'
Chose difficulty: 'Hard' you have 5 chance or 
'Easy' will have 10 chance to guess
Your Choice : """


def guessing_game():
    chances, lives = 0, 0
    secret_num = random.randint(1, 100)
    tries = input(msg).upper()
    if tries in ('HARD', 'H'):
        chances, lives = 5, 6
    elif tries in ('EASY', 'E'):
        chances, lives = 10, 11
    else:
        print("\nChoice is 'hard' or 'easy' !!!")
        print("      Try Again ! ")
        guessing_game()

    print(f"Now you have {chances} to guess the Number ")
    while chances > 0:
        guess = int(input("\nEnter your Guess: "))
        if guess == secret_num:
            print(f"\n   You Win !!!,   with {lives - chances} tries")
            break
        elif guess > secret_num:
            print(f"Too High !,  {chances - 1} Chances remaining ")
        else:
            print(f"Too Low !   {chances - 1} Chances remaining ")
        chances -= 1
    else:
        print("\n You finished all your chances . . .")
        print(f"        You Lose !")


while True:
    games = input("\n\nDo you want to play 'Number Guessing Game'? : ").upper()
    if games in ('YES', 'Y'):
        guessing_game()
    else:
        print("\n     GoodBay !")
        break























