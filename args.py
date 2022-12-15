from toml import TomlPathlibEncoder


def multiply(*numbers):  # variable number of parameters in the function
    product = 1
    for number in numbers:
        product *= number
    return product


print(multiply(3, 4, 5, 6))
