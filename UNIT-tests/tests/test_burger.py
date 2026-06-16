from burger import Burger
from unittest.mock import Mock
import pytest

class TestBurger:
# проверяем метод set_buns (корректно устанавливает булочку для бургера)
    def test_set_buns(self):
        burger = Burger()
        bun = Mock()
        burger.set_buns(bun)
        assert burger.bun == bun
# проверяем метод add_ingredient (добавляет ингридиенты в список ingredients)
    def test_add_ingredient(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        assert ingredient in burger.ingredients
# проверяем метод remove_ingredient (удаление ингридиента по индексу)
    def test_remove_ingredient(self):
        burger = Burger()
        ingredient = Mock()
        burger.add_ingredient(ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []
# проверяем метод move_ingredient (перемещение ингридиентов внутри списка)
    def test_move_ingredient(self):
        burger = Burger()
        ing1, ing2, ing3 = Mock(), Mock(), Mock()
        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
        burger.add_ingredient(ing3)
        burger.move_ingredient(0, 2)   # перемещаем первый элемент на последнюю позицию
        assert burger.ingredients == [ing2, ing3, ing1]
# проверяем метод get_price (рассчет итоговой цены)
# тестриуем три сценария (параметризация)
    @pytest.mark.parametrize(
        "bun_price, ingredient_prices, expected",
        [
            (988, [], 1976),            # флю булка (2*988)
            (988, [90], 2066),          # флю булка + соус спайси (1976+90)
            (988, [90, 300], 2366),     # флю булка + соус спайси + мин кольца (1976+90+300)
        ],
    )
    def test_get_price(self, bun_price, ingredient_prices, expected):
        burger = Burger()
# затычка на заданную цену булочки
        bun = Mock()
        bun.get_price.return_value = bun_price
        burger.set_buns(bun)
# затычка на заданные ингридиенты
        for p in ingredient_prices:
            ing = Mock()
            ing.get_price.return_value = p
            burger.add_ingredient(ing)

        assert burger.get_price() == expected
# проверить метод get_receipt (наличие всех данных в чеке)
    def test_get_receipt_contains_names_and_price(self):
        burger = Burger()
# подкидываем бургеру тестовые данные
        bun = Mock()
        bun.get_name.return_value = "Флю булка"
        bun.get_price.return_value = 988
        burger.set_buns(bun)
# подкидываем соус 
        ing1 = Mock()
        ing1.get_name.return_value = "Соус Spicy"
        ing1.get_price.return_value = 90
        ing1.get_type.return_value = "SAUCE"
# подкидываем начинку
        ing2 = Mock()
        ing2.get_name.return_value = "минеральные кольца"
        ing2.get_price.return_value = 300
        ing2.get_type.return_value = "FILLING"

        burger.add_ingredient(ing1)
        burger.add_ingredient(ing2)
# генерация чека
        receipt = burger.get_receipt()
        assert "Флю булка" in receipt
        assert "Соус Spicy" in receipt
        assert "минеральные кольца" in receipt
        assert "Price:" in receipt
        assert "2366" in receipt # 2*988+90+300
