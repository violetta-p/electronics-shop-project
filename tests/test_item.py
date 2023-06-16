import pytest
from src.item import Item
from src.phone import Phone


class NewClass(Item):
    def __init__(self, name, price, quantity):
        super().__init__(name, price, quantity)


@pytest.fixture
def example_2():
    return NewClass("Смартфон", 10000, 20)


@pytest.fixture
def example():
    return Item("Смартфон", 10000, 20)


@pytest.fixture
def example_1():
    return Phone("iPhone 14", 120_000, 5, 2)


def test_calculate_total_price(example):
    assert example.calculate_total_price() == 200000


def test_apply_discount(example):
    Item.pay_rate = 0.5
    example.apply_discount()
    assert example.price == 5000.0


def test_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item1 = Item.all[0]
    assert item1.name == 'Смартфон'


def test_string_to_number():
    assert Item.string_to_number('5') == 5
    assert Item.string_to_number('5.0') == 5
    assert Item.string_to_number('5.5') == 5.5


# Тесты к HW_3
def test_repr(example):
    assert repr(example) == "Item('Смартфон', 10000, 20)"


def test_str(example):
    assert str(example) == 'Смартфон'


# Тесты к HW_4
def test_add(example, example_1, example_2):
    assert example + example_1 == 25
    assert example_1 + example_1 == 10

    classes = (Item, Phone)
    if not isinstance(example_1, classes) or not isinstance(example, classes):
        with pytest.raises(Exception):
            example_1 + example_2
