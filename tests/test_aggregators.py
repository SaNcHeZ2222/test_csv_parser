from aggregators import aggregate_column
import pytest


def test_avg():
    data = [{'val': '2'}, {'val': '4'}, {'val': '6'}]
    result = aggregate_column(data, 'val=avg')
    assert result == {'avg(val)': 4.0}


def test_min():
    data = [{'val': '2'}, {'val': '4'}]
    result = aggregate_column(data, 'val=min')
    assert result == {'min(val)': 2.0}


def test_max():
    data = [{'val': '2'}, {'val': '4'}]
    result = aggregate_column(data, 'val=max')
    assert result == {'max(val)': 4.0}


def test_avg_valid():
    rows = [{'price': '100'}, {'price': '200'}]
    assert aggregate_column(rows, 'price=avg') == {'avg(price)': 150.0}


def test_min_valid():
    rows = [{'rating': '4.5'}, {'rating': '4.8'}]
    assert aggregate_column(rows, 'rating=min') == {'min(rating)': 4.5}


def test_max_valid():
    rows = [{'rating': '4.5'}, {'rating': '4.8'}]
    assert aggregate_column(rows, 'rating=max') == {'max(rating)': 4.8}


def test_non_numeric_column_raises():
    rows = [{'brand': 'apple'}, {'brand': 'xiaomi'}]
    with pytest.raises(ValueError, match="Invalid aggregation instruction or non-numeric column"):
        aggregate_column(rows, 'brand=avg')


def test_unsupported_operation_raises():
    rows = [{'price': '100'}, {'price': '200'}]
    with pytest.raises(ValueError, match="Unsupported aggregation operation"):
        aggregate_column(rows, 'price=median')