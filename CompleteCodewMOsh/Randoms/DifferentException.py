try:
    age = int(input('>'))
    sum = 225//age

except (ValueError, ZeroDivisionError):
    print('Exception')
# except ZeroDivisionError:
#     print("zero")

print("done")
