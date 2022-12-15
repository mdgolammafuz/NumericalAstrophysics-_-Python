# scope is a region of space in code where a value of a variable is 
# Avoid global variables, use local variables like message and parameters like name
message = "a"


def greet(name):
    global message  # bad practice
    message = "b"


def send_email(name):
    message = "c"


greet("Mafuz")
print(message)  # b will be printed
