import pytest
from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price():
    produkt = Product.new_product(
        product_list={
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    produkt.name = "Samsung Galaxy S23 Ultra"
    produkt.description = "256GB, Серый цвет, 200MP камера"
    produkt.price = 180000.0
    produkt.quantity = 5


def test_product_price_setter(capsys, product):
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"


def test_product_str(product_1):
    assert str(product_1) == "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."


def test_product_add(product_1, product_2):
    assert product_1 + product_2 == 2580000


def test_product_add_error(product_1):
    with pytest.raises(TypeError):
        product_1 + 1
