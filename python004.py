filename = open('C:/\/pydata/\/alice_in_wonderland.dat')
tot_letters = 0
tot_e = 0

bookin = filename.read()

for i in bookin:
    if i.isalnum():
        tot_letters += 1
        if i.lower() == 'e':
            tot_e += 1
print 'Total letters: %s' % format(tot_letters, ',d')
print 'Total e\'s: %s' % format(tot_e, ',d')
print '%.1f percent of all the letters are e\'s' % (100 * float(tot_e)/tot_letters)



"""def function(filename):
while True:

letter_e = 0
letters_all = 0

for line in filename:
    if filename.is_alpha and is 'e' or 'E':
        count = 0
        letter_e +1
    elif filename.is_alpha:
        count = 0
        letters_all +1



all = filename.letters()
e_total = all.count('eE')
print all
print e_total
print 100 * float(e_total)/float(all)
"""
