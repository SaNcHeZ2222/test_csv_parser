import csv
from filters import apply_filter
from aggregators import aggregate_column


def process_csv(file_path: str, where: str = None, aggregate: str = None):
    with open(file_path, encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    if where:
        rows = apply_filter(rows, where)

    if aggregate:
        return [aggregate_column(rows, aggregate)]
    else:
        return rows
