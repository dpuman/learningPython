string = 'bbbbaaammmmm'
char = ''
count = 0
max = 0

for x in string:
    for y in string:
        if x == y:
            count += 1
            # char = y

        if count > max:
            max = count
            char = y
    count = 0

print(f'char:{char} max: {max}')
