import random


def number_game():
    num_1=int(input("from ___  : "))
    num_2=int(input("to ___ : "))

    while True:
        user=int(input(f"guess a number from {num_1} to  {num_2} : "))

        random_number=random.randint(num_1,num_2)

        if user==(random_number):
            print("Correct!!" )
            break
        elif user<random_number:
            print("Too low! ")

        elif user>random_number:
            print("Too high! ")
    
        
        else:
            print(" CORRECT ! ")
            break



def ROCK_PAPER_SCISSOR():
    game_possibilities=["rock","paper","siccors"]
    computer_choice=random.choice(game_possibilities)
    while True:
        Player=input("Enter (Rock, paper or scissors: )")
        lower_user=Player.lower()
        if lower_user!=computer_choice:
            print(" OPPS !! YOU LOST! ")
        
        else:
            print("HURAY !! YOU WON!")
            break

while(True):
    print("""WELCOME TO THE GAME !
1.GUESS THE NUMBER GAME 
2.ROCK PAPER SCISSOR GAME
3.QUIT
          """)
    Player=int(input("Choose one of the above game: "))
    if Player==1:
        number_game()
    elif Player==2:
        ROCK_PAPER_SCISSOR()
    elif Player==3:
        print("Exited the program!")
        break
    else:
        print("PLEASE SELECT NUMBER BETWEEN 1-3")