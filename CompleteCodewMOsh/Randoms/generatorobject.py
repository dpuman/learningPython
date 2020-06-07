from sys import getsizeof
value = (x*2 for x in range(10))

print(value)

print("size of gen: ", getsizeof(value))
for x in value:
    print(x)

value = [x*2 for x in range(10)]
print("size of list: ", getsizeof(value))
