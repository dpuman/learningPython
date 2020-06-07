browssing_session = []
browssing_session.append(1)
browssing_session.append(2)
browssing_session.append(3)
print(browssing_session)

x = browssing_session.pop()
print(x)

print(browssing_session)
print('Redirect: ', browssing_session[-1])
if not browssing_session:
    print('disable ')
