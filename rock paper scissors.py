import random
options=("rock","paper","scissors")
player=1
while player==1:
    computer=random.choice(options).lower()
    user=input("Enter your choice(Rock,Paper,Scissors):").lower()
    print("\nUser:",user)
    print("Computer:",computer)
    if user==computer:
        print("It's a tie!")
    elif user=="rock" and computer=="scissors":
        print("You win!")
    elif user=="paper" and computer=="rock":
        print("You win!")
    elif user=="scissors" and computer=="paper":
        print("You win!")
    else:
        print("You loose!")
    player=int(input("\nPlay again?\n enter 1 to play, 0 to exit : "))