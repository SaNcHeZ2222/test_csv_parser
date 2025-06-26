from processor import process_csv
import pytest


def test_filter_and_aggregate():
    file = 'example.csv'
    result = process_csv(file, where='brand==xiaomi', aggregate='price=max')
    assert result == [{'max(price)': '299.0'}]


def test_combined_filter_aggregate(tmp_path):
    content = "brand,price\nxiaomi,100\napple,200"
    file = tmp_path / "test.csv"
    file.write_text(content)

    result = process_csv(str(file), where="brand==xiaomi", aggregate="price=max")
    assert result == [{'max(price)': '100.0'}]


def test_empty_result_after_filter(tmp_path):
    content = "brand,price\nxiaomi,100\napple,200"
    file = tmp_path / "test.csv"
    file.write_text(content)

    result = process_csv(str(file), where="brand==samsung")
    assert result == []


def test_invalid_file_path():
    with pytest.raises(FileNotFoundError):
        process_csv("no_such_file.csv")