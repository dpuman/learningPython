point = {
    'x': 1,
    'y': 2
}
print(point['x'])
pointTwo = dict(a=1, b=2, c=3)

pointTwo['a'] = 4
# new key
pointTwo['d'] = 5

if 'a' in pointTwo:
    print('Exist')

print(pointTwo.get('e', 1))


# loop

for key in pointTwo:
    print(key, pointTwo[key])

for key, value in pointTwo.items():
    print(value)
