# assigns to the variable x a string 
x = "There are %d types of people." % 10
# assigns to the variable binary the string 'binary'
binary = "binary"
# assigns to the variable do_not the string 'don't'
do_not = "don't"
# assigns to the variable y the string with the format variables embedded
y = "Those who know %s and those who %s." % (binary, do_not)

# prints the strings assigned to x and y
print x
print y

# prints the strings with the format variables
print "I said: %r." % x
print "I also said: '%s'." % y

# assigns the Boolean value False to the variable hilarious
hilarious = False
# sets joke_evaluation variable to the string with the format variable %r (no % yet)
joke_evaluation = "Isn't that joke so funny!? %r"
print joke_evaluation
# embeds the variable hilarious to the string in joke_evaluation
print joke_evaluation % hilarious

# assigns to w, e the following strings
w = "This is the left side of..."
e = "a string with a right side."

# concatenatates the two strings
print w + e
