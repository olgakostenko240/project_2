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
        elif  new_price <= 0:
            self.__price = self.__price
            print("Цена не должна быть нулевая или отрицательная")


# if __name__ == "__main__":
#product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
#product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
#product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
#print(product1.name)
#print(product1.description)
#print(product1.price)
#print(product1.quantity)
#
#print(product2.name)
#print(product2.description)
#print(product2.price)
#print(product2.quantity)
#
#print(product3.name)
#print(product3.description)
#print(product3.price)
#print(product3.quantity)
#
#new_product = Product.new_product(
#{"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
#"quantity": 5})
#
#print(new_product.name)
#print(new_product.description)
#print(new_product.price)
#print(new_product.quantity)
#
#new_product.price = 800
#print(new_product.price)

#new_product.price = -100
#print(new_product.price)
#new_product.price = 0
#print(new_product.price)
