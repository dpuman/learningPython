numbers = [1, 1, 2, 3, 4]
first = set(numbers)
second = {1, 5}
print(len(second))

hudai = {1, 2, 3, 4, 5}
hudai.remove(1)
hudai.add(10)
print(hudai)
# union
print(first | second)
# intersection
print(first & second)
# difference
print(first-second)
# SemetricDefference
print(first ^ second)
