import random
def guess_number(user,right_guess):
    if user==right_guess:
        print("right guess!!")
    elif user>right_guess:
        print("user guess is bit high!")
    elif user < right_guess:
        print("your guess is bit low!")
    else:
        print("invalid input!")

right_guess=random.randint(1,15)
chances=5
while chances!=0:
      print(f"{chances} chances left...")
      user_guess=int(input('Enter your guess(1-15):'))
      guess_number(user_guess,right_guess)
      chances-=1


