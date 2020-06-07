products = [
    ('tamanna', 10),
    ('tabassum', 5),
    ('mony', 20)
]

new_product_list = list(map(lambda item: item[1], products))
# usingCompraenssion
com_product_list = [item[1] for item in products]

new_filter_list = list(filter(lambda item: item[1] >= 10, products))
com_filter_list = [item for item in products if item[1] >= 10]

print(new_product_list, new_filter_list)
print(com_product_list, com_filter_list)
