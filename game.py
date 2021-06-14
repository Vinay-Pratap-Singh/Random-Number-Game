import random

def game_easy():
    count=0
    guess_number=random.randint(1,50)
    number=0
    while number!=guess_number:
        number=int(input("Guess the Number: "))
        if number>50 or number<1:
            print("Enter a number between 1 and 50 only")
            game_easy()
        elif number>guess_number:
            print("Choose a Smaller One")
        elif number<guess_number:
            print("Choose a Larger One")
        count=count+1
    print("Congrats!!!!!\nYou won the Game")
    print(f"Total Attempt = {count}")
    
    with open("high_score.txt",) as f:
        score=f.read()
        if int(score)==0:
            with open("high_score.txt","w") as f:
                f.write(str(count))
        elif int(score)>count:
            with open("high_score.txt","w") as f:
                f.write(str(count))
    count=0    
    high_score()


def game_medium():
    count=0
    guess_number=random.randint(1,100)
    number=0
    while number!=guess_number:
        number=int(input("Guess the Number: "))
        if number>100 or number<1:
            print("Enter a number between 1 and 100 only")
            game_medium()
        elif number>guess_number:
            print("Choose a Smaller One")
        elif number<guess_number:
            print("Choose a Larger One")
        count=count+1
    print("Congrats!!!!!\nYou won the Game")
    print(f"Total Attempt = {count}")
    
    with open("high_score.txt",) as f:
        score=f.read()
        if int(score)==0:
            with open("high_score.txt","w") as f:
                f.write(str(count))
        elif int(score)>count:
            with open("high_score.txt","w") as f:
                f.write(str(count))
    count=0    
    high_score()


def game_hard():
    count=0
    guess_number=random.randint(1,500)
    number=0
    while number!=guess_number:
        number=int(input("Guess the Number: "))
        if number>500 or number<1:
            print("Enter a number between 1 and 500 only")
            game_easy()
        elif number>guess_number:
            print("Choose a Smaller One")
        elif number<guess_number:
            print("Choose a Larger One")
        count=count+1
    print("Congrats!!!!!\nYou won the Game")
    print(f"Total Attempt = {count}")
    
    with open("high_score.txt",) as f:
        score=f.read()
        if int(score)==0:
            with open("high_score.txt","w") as f:
                f.write(str(count))
        elif int(score)>count:
            with open("high_score.txt","w") as f:
                f.write(str(count))
    count=0    
    high_score()


def level():
    print("\n1: Easy\n2: Medium\n3: Hard\n")
    option=int(input("Select a Level: "))
    if option==1:
        game_easy()
    elif option==2:
        game_medium()
    elif option==3:
        game_hard()
    else:
        print("Please select a valid Option")
        level()

def high_score():
    with open("high_score.txt") as f:
            score=f.read()
            print(f"Best Score (Won in Least Attempt): {score}")
    menu()

def menu():
    print("\n*****Welcome to the Random Number Game*****\n")
    print("1: Start Game\n2: Level\n3: High Score\n4: Instruction\n5: Exit\n")

    option=int(input("Select the Option: "))
    if option==1:
        game_easy()
    elif option==2:
        level()
    elif option==3:
        high_score()
    elif option==4:
        with open("instruction.txt") as f:
            myinst=f.read()
            print(myinst)
        menu()
    elif option==5:
        exit(0)
    else:
        print("Please enter a Valid Option\n")
        menu()     

menu()