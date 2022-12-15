# program to quit from python interactive cell to terminal
command = ""
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)
