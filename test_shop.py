"""
Протестируйте классы из модуля homework/models.py
"""
import pytest

from models import Product, Cart


@pytest.fixture
def cart(product):
    cart = Cart()
    return cart


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(0) is True
        assert product.check_quantity(100) is True
        assert product.check_quantity(500) is True
        assert product.check_quantity(1001) is False

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(600)
        assert product.quantity == 400

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError):
            product.buy(1001)
            assert pytest.raises(ValueError)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """

    def test_add_product(self, product, cart):
        cart.add_product(product, 5)
        assert cart.products[product] == 5

    def test_add_product_negative(self, product, cart):
        with pytest.raises(ValueError):
            assert cart.add_product(product, 0) is ValueError


    def test_remove_product_more_available(self, cart, product):
        cart.add_product(product, 1000)
        cart.remove_product(product, 1001)
        assert cart.products.get(product, None) is None

    def test_remove_product_nothing(self, product, cart):
        with pytest.raises(ValueError):
            cart.remove_product(product)

    def test_remove_product_part(self, cart, product):
        cart.add_product(product, 500)
        cart.remove_product(product, 100)
        assert cart.products.get(product, None) == 400

    def test_clear(self, product, cart):
        cart.add_product(product)
        cart.clear()
        assert cart.products == {}

    def test_get_total_price(self, product, cart):
        cart.add_product(product, 5)
        total_price = cart.get_total_price()
        assert total_price == 500

    def test_buy(self, product, cart):
        cart.add_product(product, 100)
        cart.buy()
        assert product.quantity == 900

        cart.add_product(product, quantity=100)
        cart.buy()
        assert product.quantity == 800

        cart.add_product(product, quantity=800)
        cart.buy()
        assert product.quantity == 0

    def test_buy_negative(self, product, cart):
        cart.add_product(product, 1001)
        with pytest.raises(ValueError):
            cart.buy()