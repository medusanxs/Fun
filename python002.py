x = 'himalayas'
print len(x)
print x[2:]
print x[-1]
print x[:-1]

print x[2:7:2]

y = 'hi'
print y
print id(y)
y = y + 'ya'
print y
print id(y)

print "jason put titty sprinkles on that B"

#def find(word, letter):
#    index = 0
#    while index < len(word):
#	if word[index] == letter:
#	    return index


word = raw_input("enter a word:")
letter_to_find = raw_input( "enter a letter to find in the word: ")
count = 0
for letter in word:
    if letter == letter_to_find:
        count += 1
print "found", count, "occurences of", letter_to_find

x = 'himalayas'
print x.upper()
print x.lower()
print x.find("ya")
print x.count("a")
print x.startswith("hi")
print x.endswith("as")

#wordski
