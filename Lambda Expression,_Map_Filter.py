# Function to compute square
def square(num):
    return num**2


# Function call using its name 'square' and a required parameter
print(square(4))

# Let’s rearrange the above function "square" in a single line.


def square2(num): return num**2


print(square2(4))


print(lambda num: num*2)
# We will use this expression in map and filter to understand it in more detail

my_list = [1, 2, 3, 4, 5]
num_sq = []
for num in my_list:
    num_sq.append(num**2)
print(num_sq)


result = map(square, my_list)
print(list(result))
# list(map(square, my_list)) # in a single line!

my_list = [1, 2, 3, 4, 5]
# casting to the list to get the result back
my_new_list = list(map(lambda num: num**2, my_list))
print(my_new_list)


a = [1, 2, 3, 4]
b = [17, 12, 11, 10]
c = [-1, -4, 5, 9]
#list(map(lambda a, b, c : a + b + c, a, b, c))
my_list = list(map(lambda x, y, z: x + y + z, a, b, c))
print(my_list)

# "we’re using the range function here!"
print(list(filter(lambda num: num % 2 == 0, range(1, 10))))
# casting to the list to get ,the result back
