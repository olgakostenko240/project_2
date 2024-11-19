import pytest
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


def test_category_str(category):
    assert str(category) == "Смартфоны, количество продуктов: 11 шт."


def test_product_iterator(product_iterator):
    iter(product_iterator)
    assert product_iterator.index == 0
    assert next(product_iterator).name == "Samsung Galaxy S23 Ultra"
    assert next(product_iterator).name == "Iphone 15"
    assert next(product_iterator).name == "Xiaomi Redmi Note 11"

    with pytest.raises(StopIteration):
        next(product_iterator)

def test_add_product_1():
    category_test = Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        products=[]
    )

    with pytest.raises(TypeError):
        category_test.add_product("Not a product")


def test_category_smartphone_product(category, product_smartphone_1):
    category.new_product = product_smartphone_1
    assert category.products_in_list[-1].name == "Xiaomi Redmi Note 11"