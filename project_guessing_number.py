import random
import math
def guess_number():
    print("Are you Excited the Play Guess number Game!")
    first_number=int(input("Enter the first numner:"))      #1
    second_number=int(input("Enter the Second number:"))    #100
    random_number=random.randint(first_number,second_number)
    print("random Number is:",random_number)
    for i in range(100):    #attempts
        print("Guess the Random Number between",first_number,"and",second_number)
        guess=int(input("Guess:"))
        if guess==random_number:
            print("Congrats Buddy!, You did it.")
            print("----------------------------")
            break;
        elif guess>random_number:
            print("Too High....Try Again!")
            print("----------------------")
        else:
            print("Too Low....Try Again!")
            print("-----------------------")
guess_number()
