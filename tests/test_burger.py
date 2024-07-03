from unittest.mock import Mock
import praktikum.ingredient_types
import praktikum
from praktikum.burger import Burger, Bun
from praktikum.database import Database


class TestBurger:

    def test_set_buns(self):
        burger = Burger()
        bun = Bun('Краторная булка N-200i', 1255)
        burger.set_buns(bun)
        assert burger.bun == bun

    def test_add_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        mock_ingredient.get_name.return_value = 'Краторная булка N-200i'
        mock_ingredient.get_price.return_value = 1255
        mock_ingredient.get_type.return_value = praktikum.ingredient_types.INGREDIENT_TYPE_FILLING
        burger.add_ingredient(mock_ingredient)
        assert burger.ingredients[0].get_price() == 1255
        assert burger.ingredients[0].get_name() == 'Краторная булка N-200i'
        assert burger.ingredients[0].get_type() == praktikum.ingredient_types.INGREDIENT_TYPE_FILLING

    def test_delete_ingredient(self):
        burger = Burger()
        mock_ingredient = Mock()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert len(burger.ingredients) == 0

    def test_get_price(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[4])
        assert burger.get_price() == 500

    def test_get_receipt(self):
        burger = Burger()
        database = Database()
        burger.set_buns(database.available_buns()[0])
        burger.add_ingredient(database.available_ingredients()[0])
        burger.add_ingredient(database.available_ingredients()[3])
        get_receipt = "(==== black bun ====)\n" \
                      "= sauce hot sauce =\n" \
                      "= filling cutlet =\n" \
                      "(==== black bun ====)\n\n" \
                      "Price: 400"
        assert get_receipt == burger.get_receipt()
