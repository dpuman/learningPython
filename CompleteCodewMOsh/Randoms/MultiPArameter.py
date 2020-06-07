def multiply(*numbers):
    total = 1
    for numer in numbers:
        total *= numer
    return total


print('Okay')
print(multiply(2, 3, 4))
