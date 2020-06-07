items = [
    ('Tabassum', 2),
    ('mony', 3),
    ('Tamanna', 1),
]


def short_items(item):
    return item[1]


items.sort(key=short_items)
print(items)
