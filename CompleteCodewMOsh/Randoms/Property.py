class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Invalide price")
        else:
            self.__price = value

    # price = property(get_price, set_price)


product = Product(-10)
print(product.price)
# product.price = -10
