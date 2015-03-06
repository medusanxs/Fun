filename = open('C:\pydata\alice_in_wonderland.dat','r')


all = filename.ascii_letters
e_total = filename.count('e')
print all
print e_total
print 100 * float(e_total)/float(all)
