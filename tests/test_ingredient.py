import pytest
from praktikum.ingredient import Ingredient
from praktikum.ingredient_types import *


class TestIngredient:

    def test_get_correct_price(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_price() == 88

    def test_get_correct_name(self):
        ingredient = Ingredient(INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88)
        assert ingredient.get_name() == 'Соус с шипами Антарианского плоскоходца'

    @pytest.mark.parametrize(
        'type, name, price, expected_ingredient',
        [
            [INGREDIENT_TYPE_SAUCE, 'Соус с шипами Антарианского плоскоходца', 88, 'SAUCE'],
            [INGREDIENT_TYPE_FILLING, 'Мясо бессмертных моллюсков Protostomia', 1337, 'FILLING']
        ]
    )
    def test_get_correct_type(self, type, name, price, expected_ingredient):
        ingredient = Ingredient(type, name, price)
        assert ingredient.get_type() == expected_ingredient
