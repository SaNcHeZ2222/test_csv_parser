from filters import apply_filter
import pytest


def test_equal_filter():
    data = [{'a': '1'}, {'a': '2'}]
    result = apply_filter(data, 'a==2')
    assert result == [{'a': '2'}]


def test_greater_filter():
    data = [{'a': '1'}, {'a': '3'}]
    result = apply_filter(data, 'a>2')
    assert result == [{'a': '3'}]


def test_less_filter():
    data = [{'a': '1'}, {'a': '3'}]
    result = apply_filter(data, 'a<2')
    assert result == [{'a': '1'}]


def test_equal_filter_text():
    data = [{'brand': 'apple'}, {'brand': 'xiaomi'}]
    assert apply_filter(data, 'brand==apple') == [{'brand': 'apple'}]


def test_greater_filter_valid():
    data = [{'price': '100'}, {'price': '200'}]
    assert apply_filter(data, 'price>150') == [{'price': '200'}]


def test_less_filter_valid():
    data = [{'rating': '4.5'}, {'rating': '4.2'}]
    assert apply_filter(data, 'rating<4.4') == [{'rating': '4.2'}]


def test_non_numeric_greater_raises():
    data = [{'brand': 'apple'}, {'brand': 'samsung'}]
    with pytest.raises(ValueError, match="Filter value 'apple' for column 'brand' must be a number"):
        apply_filter(data, 'brand>apple')


def test_invalid_filter_syntax():
    data = [{'a': '1'}]
    with pytest.raises(ValueError, match="Invalid filter condition"):
        apply_filter(data, 'a!=1')
