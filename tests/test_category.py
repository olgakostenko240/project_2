from src.category import Category
from src.product import Product


def test_category_init(category, category_1):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category.products_in_list) == 3

    assert category.product_count == 4
    assert category_1.product_count == 4

    assert category.category_count == 2
    assert category_1.category_count == 2


def test_add_product():
    category_test = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[]
    )
    product_test = Product(
        name="Iphone 15",
        description="512GB, Gray space",
        price=210000.0,
        quantity=8
    )
    category_test.add_product(product_test)

    assert category_test.product_count == 5


def test_list_product_property(category):
    assert category.products == ("Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n"
                                 "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n"
                                 "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n")
