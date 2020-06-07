first = [1, 2, 3]
second = [4, 5, 6]

print(*first)

values = [*first, *'hello', *second]
print(values)
# for Dictionary

firstd = dict(x=1, y=2, z=3)
SecondD = dict(a=8, b=9, c=10)

combine = {**firstd, 'key': 100, **SecondD}
print(combine)
