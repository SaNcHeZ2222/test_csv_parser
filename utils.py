from typing import List, Dict
from tabulate import tabulate


def print_table(data: List[Dict[str, str]]):
    if not data:
        print("No data")
    else:
        print(tabulate(data, headers="keys", tablefmt="github"))
