import pytest
from src.phone import Phone


@pytest.fixture
def example_phone():
    return Phone("iPhone 14", 120_000, 5, 2)


@pytest.fixture
def example_phone_1():
    return Phone("iPhone 14", 120_000, 5, 0)


def test_repr(example_phone):
    assert str(example_phone) == 'iPhone 14'
    assert repr(example_phone) == "Phone('iPhone 14', 120000, 5, 2)"
    assert example_phone.number_of_sim == 2


def test_number_of_sim(example_phone_1):
    with pytest.raises(Exception):
        assert example_phone_1.number_of_sim
