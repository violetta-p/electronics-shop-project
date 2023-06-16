import pytest
from src.keyboard import Keyboard


@pytest.fixture
def example_kb():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_str(example_kb):
    assert str(example_kb) == "Dark Project KD87A"


def test_change_lang(example_kb):
    assert str(example_kb.language) == "EN"
    example_kb.change_lang()
    assert str(example_kb.language) == "RU"
    example_kb.change_lang()
    assert str(example_kb.language) == "EN"
    with pytest.raises(AttributeError):
        example_kb.language = 'CH'
