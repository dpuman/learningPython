try:
    age = int(input('>'))
except ValueError as ar:
    print(ar)
    print(type(ar))
    print('Exception')
else:
    print("Else")
print("done")
