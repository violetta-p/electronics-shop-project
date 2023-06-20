import pytest
from src.item import Item, InstantiateCSVError
from src.phone import Phone

NORMAL_FILE = "items.csv"
NON_EXISTENT_FILE = "item1.csv"
KEY_ERROR_FILE = "item(key_er).csv"
VALUE_ERROR_FILE = "item(val_er).csv"
MISSING_DATA_FILE = "item(missing).csv"


class NewClass:
    def __init__(self, name, price, quantity):
        self.__name = name
        self.price = price
        self.quantity = quantity


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


def test_repr(example):
    assert repr(example) == "Item('Смартфон', 10000, 20)"


def test_str(example):
    assert str(example) == 'Смартфон'


def test_add(example, example_1, example_2):
    assert example + example_1 == 25
    assert example_1 + example_1 == 10

    classes = (Item, Phone)
    if not isinstance(example_2, classes):
        with pytest.raises(Exception):
            example_1 + example_2


def test_exceptions():
    Item.csv_file_name = NON_EXISTENT_FILE
    with pytest.raises(FileNotFoundError):
        Item.instantiate_from_csv()

    Item.csv_file_name = KEY_ERROR_FILE
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()

    Item.csv_file_name = VALUE_ERROR_FILE
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()

    Item.csv_file_name = MISSING_DATA_FILE
    with pytest.raises(InstantiateCSVError):
        Item.instantiate_from_csv()
