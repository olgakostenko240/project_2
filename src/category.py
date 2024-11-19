from src.product import Product


class Category:
    name: str
    description: str
    products: list
    product_count = 0
    category_count = 0


    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        Category.product_count += len(products)
        Category.category_count += 1


    def __str__(self):
        return f"{self.name}, количество продуктов: {self.product_count} шт."


    def add_product(self, new_product: Product):
        self.__products.append(new_product)
        Category.product_count += 1


    @property
    def products(self):
        product_str = ""
        for product in self.__products:
            product_str += f"{str(product)}\n"
        return product_str


    @property
    def products_in_list(self):
        return self.__products


# if __name__ == "__main__":
# product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
# product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
# product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
# category1 = Category(
# "Смартфоны",
# "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
# [product1, product2, product3]
# )
#
# print(str(category1))
#
# print(category1.products)
#
# print(product1 + product2)
# print(product1 + product3)
# print(product2 + product3)
#
# print(category1.products)
# product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
# category1.add_product(product4)
# print(category1.products)
# print(category1.product_count)
# print(category1.category_count)
# product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
# product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
# product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
#
# category1 = Category(
# "Смартфоны",
# "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
# [product1, product2, product3]
# )
#
# print(category1.name)
# print(category1.description)
# print(len(category1.products))
# print(category1.category_count)
# print(category1.product_count)
#
# product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
# category2 = Category(
# "Телевизоры",
# "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
# [product4]
# )
#
# print(category2.name)
# print(category2.description)
# print(len(category2.products))
#
# print(Category.category_count)
# print(Category.product_count)
