String = "Hey, I am James"
# default sep, which is a white space.
print(String.split())

tweet = 'Go Flames Go! #Hockey'
# splitting tweet at #....
print(tweet.split('#'))  # or (sep = '#')

# We can grab any element with split and then indexing
print(tweet.split('#')[0])
print(tweet.split('#')[1])
# print(tweet.split('#')[2])  # IndexError: list index out of range
