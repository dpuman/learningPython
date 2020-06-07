from array import array

numbers = array('i', [1, 2, 3])
numbers.append(4)
numbers.insert(0, 10)

print(numbers)
numbers.pop()
numbers.remove(2)
print(numbers[0])
numbers[0] = 40
print(numbers)
