import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING
from praktikum.ingredient import Ingredient

@pytest.mark.parametrize(
    "ingredient_type, name, price",
    [
        (INGREDIENT_TYPE_SAUCE, "Hot Sauce", 50.0),
        (INGREDIENT_TYPE_SAUCE, "Chili Sauce", 60.0),
        (INGREDIENT_TYPE_FILLING, "Cutlet", 100.0),
        (INGREDIENT_TYPE_FILLING, "Cheese", 150.0)
    ]
)
class TestIngredientMethods:


    def test_get_name(self, ingredient_type, name, price):

        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_name() == name, f"Ожидалось название '{name}', но получено {ingredient.get_name()}"

    def test_get_price(self, ingredient_type, name, price):

        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_price() == price, f"Ожидалась цена {price}, но получена {ingredient.get_price()}"

    def test_get_type(self, ingredient_type, name, price):

        ingredient = Ingredient(ingredient_type, name, price)
        assert ingredient.get_type() == ingredient_type, f"Ожидался тип {ingredient_type}, но получен {ingredient.get_type()}"

