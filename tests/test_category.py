def test_category_init(category, category_1):
    assert category.name == "Смартфоны"
    assert (
        category.description
        == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    )
    assert len(category.products) == 3

    assert category.product_count == 4
    assert category_1.product_count == 4

    assert category.category_count == 2
    assert category_1.category_count == 2
