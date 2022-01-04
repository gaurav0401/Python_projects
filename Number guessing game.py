import random
def check_guess(user_guess , right_guess):
    if user_guess==right_guess:
        return True



def get_userguess():
    guess=int(input('Enter your guess[1-25]:'))
    return guess



def play_menu():
    print("----------Number Guessing----------")
    print("1.Play")
    print("2.Exit")

def hints(right_guess,user_guess):
    if user_guess%2!=0 and right_guess%2==0:
        return "Hint: Right guess is a multiple of 2(try again)"
    elif right_guess <user_guess:
        return "Hint: your guess is bit high (try again)"
    elif right_guess > user_guess:
        return "Hint: your guess is bit low (try again) "


def main():
    play_menu()
    print(17*"-*")
    ch=input("Enter your choice:")
    right_guess=random.randint(1,25)
    score=0
    if ch=='1':
        play='y'
        while play=='y':
            user_guess=get_userguess()
            win=check_guess(user_guess,right_guess)
            if win == True:
                print("Well Played!!!")
                score+=4
                print("You got 4 points...\nScore:",score)
                right_guess=random.randint(1,25)

            else:
                score-=1
                print("You lost 1 point...\nScore:",score)
                print(hints(right_guess,user_guess))
            print(40*"_")
            play=input("do you wanna play again....(y/n):")
            print(40*"_")

    elif ch=='2':
        print("closing a game.....")
        exit()

main()


