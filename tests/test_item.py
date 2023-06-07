import pytest
from src.item import Item


@pytest.fixture
def example():
    return Item("Смартфон", 10000, 20)


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
