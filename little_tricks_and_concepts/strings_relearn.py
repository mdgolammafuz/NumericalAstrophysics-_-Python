# STRINGS :

# creating single quotes string
string_example = 'creating single quotes string'

# creating double quotes string
string_example_2 = "creating double quotes string"

# we have lots of other quotes, let's wrap them in double quotes
string_example_3 = "we have lots of other quotes, let's wrap them in double quotes"

print(string_example)
print(string_example_2)
print(string_example_3)


name = 'Mafuz'
number = 32
print('My name is {one} and my number is {two}'.format(one=name, two=number))


name = 'Mafuz'
number = 32
print('My name is {one} and my number is {two}, {one} again and {two} again'
      .format(one=name, two=number))


# Let's create a string
X = "MAFUZ"

# grabbing the first letter in the String
print('First Letter in the String : {}'.format(X[0]))

# grabbing the last letter
print('Last Letter in the String : {}'.format(X[-1]))


# IndexError exception

# city = 'Burdwan'
# print(city[7])


first_name = "Golam "
last_name = "Mafuz"
# concatenation of String
full_name = first_name + last_name
print(full_name)


# Assign 'Mafuz' to friend.
friend = 'Mafuz'
# Can we change the first character to 'J'?
# friend[0] = 'J'  # No, this will cause an error!

X = "String"
# grabbing a slice (everything after index 1)
print(X[1:])

# grabbing a slice (everything from index 0 upto 4 (not included))
print(X[:4])

# grabbing a slice (with first and last given positions)
print(X[0:4])

String = "Hey, I am James"
# Actual String
print("Actual String : {}".format(String))

# printing in lower case
print("Lower Case : {}".format(String.lower()))

# printing in upper case
print("Upper Case : {}".format(String.upper()))

String = "Hey, I am James"
# default sep, which is a white space.
print(String.split())

tweet = 'Go Flames Go! #Hockey'
# splitting tweet at #....
print(tweet.split('#'))  # or (sep = '#')

# We can grab any element with split and then indexing
print(tweet.split('#')[1])
