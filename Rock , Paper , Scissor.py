import random

def menu():
    print(10*"-","Rock paper Scissor",10*"-")
    print("1.play")
    print("2.exit")

def play():
    p_score=0
    c_score=0
    play='y'
    while play=='y':
        user=input("Enter your choice['rock','paper','scissor']:")
        computer=random.choice(['rock','paper','scissor'])
        print(f"user choice: {user} || computer choice: {computer}")
        if user == computer:
            print("Tie!")
        elif user=="rock":
            if computer=="scissor":
                p_score+=1
                print("user wins!!!")
            else:
                c_score+=1
                print("Computer wins!!!")
        elif user=="paper":
            if computer=="rock":
                p_score+=1
                print("user wins!!!")
            else:
                c_score+=1
                print("Computer wins!!!")
        elif user=="scissor":
            if computer=="paper":
                p_score+=1
                print("user wins!!!")
            else:
                c_score+=1
                print("Computer wins!!!")
        else:
            print("Please enter choice between['rock','paper','season']")
            exit()
        print(f"player score:{p_score} || computer score:{c_score}")
        print(20*"__")
        play=input("Do you want to play continue(y/n)?:")
        print(20*"**")

def main():
    menu()
    print(20*"__")
    ch=input("Enter your choice:")
    print(20*"__")
    if ch=="1":
        play()
    elif ch=="2":
        exit()
    else:
        print("invalid input...")

main()