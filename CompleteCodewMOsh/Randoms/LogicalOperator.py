high_income = True
good_credit = False
student = False

message = ''

if (high_income or good_credit) and not student:
    message = 'Eligable'
else:
    message = 'Not Eligable'

print(message)
