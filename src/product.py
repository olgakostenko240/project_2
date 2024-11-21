class Product:
    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(other) is Product:
            return self.__price * self.quantity + (other.__price * other.quantity)
        else:
            raise TypeError

    @classmethod
    def new_product(cls, product_list):
        name = product_list.get("name")
        description = product_list.get("description")
        price = product_list.get("price")
        quantity = product_list.get("quantity")
        return cls(name, description, price, quantity)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price > 0:
            self.__price = new_price
        elif new_price <= 0:
            self.__price = self.__price
            print("Цена не должна быть нулевая или отрицательная")
