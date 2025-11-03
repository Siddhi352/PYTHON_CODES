import random
print("-_-_-_ROCK PAPER SCISSORS-_-_-_")
Computer=("Rock","Paper","Scissors")
score=0
win_score=int(input("💎Enter the winning score:"))
while score!=win_score:
    print("The computer has chosen already")
    pick=input("What do YOU choose?:").lower()
    chosen=random.choice(Computer)
    #winning conditions
    if chosen=="Rock" and pick=="paper":
        print("😎YOU SCORED!😎")
        score+=1
        print()

    elif chosen=="Paper" and pick=="Scisscors":
        print("😎YOU SCORED!😎")
        score+=1
        print()

    elif chosen=="Scissors" and pick=="Rock":
        print("😎YOU SCORED!😎")
        score+=1
        print()  
    #loosing conditions
    elif chosen=="Paper" and pick=="Rock":
        print("🙂YOU LOST A POINT🙂")
        score-=1
        print()  

    elif chosen=="Scissors" and pick=="Paper":
        print("🙂YOU LOST A POINT🙂")
        score-=1
        print()  

    elif chosen=="Rock" and pick=="Scissors":
        print("🙂YOU LOST A POINT🙂")
        score-=1
        print() 

    else:
        print("😗Hmm....Tie!😗")   

        print("✨YOUR CURRENT SCORE IS{score}✨")

        print("🎉YOU WIN!🎉")

        print("----THANKS FOR PLAYING----")
              