from praktikum.database import Database


class TestDatabase:

    def test_get_available_buns(self):
        data_bun = Database()
        available_buns = data_bun.available_buns()
        assert len(available_buns) == 3

    def test_get_available_ingredients(self):
        data_ingredients = Database()
        available_ingredients = data_ingredients.available_ingredients()
        assert len(available_ingredients) == 6
