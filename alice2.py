"""file = open('C:/pydata/alice_in_wonderland.dat')

alice = []

alice.append(file.lower())
for i in alice:
    if i in alice:

"""

from string import punctuation
print punctuation #scaffolding

alice_words = {}
fin = open('c:/pydata/alice_in_wonderland.dat')
bookin = fin.read()
for i in punctuation:
    bookin = bookin.replace(i, ' ')
bookin = bookin.lower()
wordlist = bookin.split()
for word in wordlist:
    if word not in alice_words:
        alice_words[word] = 1
    else:
        alice_words[word] += 1
templist1 = alice_words.items()
counter = 0
while True:
    print templist1[counter]
    counter += 1
    if counter >20:
        break
templist2 = []
for a, b in templist1:
    templist2.append((b, a))
counter = 0
while True:
    print templist2[counter]
    counter += 1
    if counter > 20:
        break
templist2.sort()
templist2.reverse()
counter = 0
for a, b in templist2:
    print a, b
    counter += 1
    if counter > 20:
        break
print "we're done"

