from random import randint


balance = 100
dice = int(randint(1, 12))
x = dice
def roll1(x):
    for int in x:
        if x == 7:
            print x + "Lose!" + (balance - 10)
        elif x == 11:
            print x + "Win!" + (balance + 10)
        elif x == 2 or x == 3 or x == 12:
            print x + "Lose!" + (balance - 10)
        elif x == 1 or x == 4 or x == 6 or x == 8 or x == 9:
            print x + "Point" + (balance + 10)
            return roll1 + answer

def roll_other(x):
    for int in x:
        if x == 7:
            print x + "Lose!" + (balance - 10)
        elif x == 1 or x == 4 or x == 6 or x == 8 or x == 9 or x == 2 or x ==3 or x == 12:
            print x + "Point" + (balance + 10)
            return roll_other + answer

def first_roll:
    answer = raw_input("Would you like to roll again?").lower
    print answer
    while answer == 'y' or answer == 'yes':
        if dice != 7 or 11 or 2 or 3 or 12:
            print dice + (balance + 10) + answer
        elif dice == 2 or 3 or 12 or 7:
            print dice + (balance - 10) + answer
        elif answer == 'n' or answer == 'no':
            print 'Goodbye!'
            exit(0)

def consecutive_roll(roll_other):
    answer = raw_input("Would you like to roll again?").lower
    print answer
    while answer == 'y' or answer == 'yes':
        if roll_other == 7:
            print x + "Lose!" + answer
        elif roll_other == 1 or 4 or 6 or 8 or 9 or 2 or 3 or 12:
            print x + "Point"


