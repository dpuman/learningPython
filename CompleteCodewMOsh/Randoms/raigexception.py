def age(number):
    if number <= 0:
        raise ValueError("Zeroerror")
    return 10/age


try:
    age(-1)
except ValueError as er:
    print(er)
