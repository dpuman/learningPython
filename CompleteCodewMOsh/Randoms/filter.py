items = [
    ('Tabassum', 2),
    ('mony', 3),
    ('Tamanna', 1),
]

new_list = list(filter(lambda item: item[1] >= 2, items))
print(new_list)
