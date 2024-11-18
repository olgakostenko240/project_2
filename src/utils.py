import json
import os
from typing import Any

from src.product import Product
from src.category import Category


def read_json(path: str) -> dict:
    """Функция для чтения json файла"""
    full_path = os.path.abspath(path)
    with open(full_path, "r", encoding="UTF-8") as file:
        data: dict[Any, Any] = json.load(file)
    return data


def create_objects_from_json(data: Any) -> list:
    """Функция для подгрузку данных по категориями и товарам из файла JSON"""
    products_list = []
    for product_list in data:
        prod_list = []
        for prod_dict in product_list["products"]:
            prod_list.append(Product(**prod_dict))
        product_list["products"] = prod_list
        products_list.append(Category(**product_list))
    return products_list


if __name__ == "__main__":
    result = read_json("../data/products.json")
    result_data = create_objects_from_json(result)

    print(result_data[0].name)
    print(result_data[0].products)
