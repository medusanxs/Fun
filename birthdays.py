import random
"""
lst = [([random.randint(range(1,31,32)), random.randint(range(1,366,366))] * 23)]

print lst

#def has_duplicates:():


x = [random.randint(0,12) for r in xrange(23)]
y = [random.randint(0,32) for r in xrange(23)]
def day():
    for i in x:
        if i > 0:
            print i + y
        elif i == 0:
            print 'is bad'


#def has_duplicates():
 #   try:



#this is close to working!
x = [random.randint(0,12) for r in xrange(23)]
y = [random.randint(0,32) for r in xrange(23)]



def birthdays():
    while True:
        for i in x:
            print i, '+',
            for i in y:
                print i

print birthdays()
#end


        for m in x:
            m = [random.randint(0,13) for r in xrange(1)]
        for d in y:
            d = [random.randint(0,32) for r in xrange(1)]

    print m, '/', d"""


"""
from random import randint

bday = []
for i in range(23):
    bday.append(randint(1,365))

def has_dups(bdays):
    for i in bdays:
        if bdays.count(x) > 1:
            return True
"""

from random import randint

def has_duplicates(the_list):
    """checks given list for duplicates and returns True if so"""
    for i in the_list:
        if the_list.count(i) > 1:
            return True

if '_name_' == "_main_":

    same_birthday_counter = 0
    trials = 100
    for trial in range(trials):
        birthdays = []
        for b in range(23):
            birthdays.append(randint(1,365))

        if has_duplicates(birthdays):
            same_birthday_counter +=1

    print "%d sets of 23 people had the same birthday in %d trials" % same_birthday_counter, trials
