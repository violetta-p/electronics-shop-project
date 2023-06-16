import pytest
from src.phone import Phone


@pytest.fixture
def example_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def example_phone_1():
    return Phone("iPhone 14", 120_000, 5, 0)


@pytest.fixture
def example_phone_2():
    return Phone("iPhone 14", 120_000, 5, -1)


def test_repr(example_phone):
    assert repr(example_phone) == "Phone('iPhone 14', 120000, 5, 2)"


def test_str(example_phone):
    assert str(example_phone) == "iPhone 14"


def test_number_of_sim(example_phone, example_phone_1):
    assert example_phone.number_of_sim == 2

    with pytest.raises(ValueError):
        example_phone_1.number_of_sim = 0
