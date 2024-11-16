from src.product import Product


def test_product_init(product):
    assert product.name == "Samsung Galaxy S23 Ultra"
    assert product.description == "256GB, Серый цвет, 200MP камера"
    assert product.price == 180000.0
    assert product.quantity == 5


def test_product_price():
    produkt = Product.new_product(product_list={"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    produkt.name = "Samsung Galaxy S23 Ultra"
    produkt.description = "256GB, Серый цвет, 200MP камера"
    produkt.price = 180000.0
    produkt.quantity = 5


def test_product_price_setter(capsys, product):
    product.price = 0
    message = capsys.readouterr()
    assert message.out.strip() == "Цена не должна быть нулевая или отрицательная"
