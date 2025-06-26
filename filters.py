from typing import List, Dict


def apply_filter(rows: List[Dict[str, str]], condition: str) -> List[Dict[str, str]]:
    def is_float(value: str, col: str) -> float:
        try:
            return float(value)
        except ValueError:
            raise ValueError(f"Non-numeric value '{value}' in column '{col}' for numeric comparison")


    if '==' in condition:
        col, val = condition.split('==', 1)
        return [row for row in rows if row[col] == val]

    elif '>' in condition:
        col, val = condition.split('>', 1)
        try:
            val = float(val)
        except ValueError:
            raise ValueError(f"Filter value '{val}' for column '{col}' must be a number")
        return [row for row in rows if is_float(row[col], col) and float(row[col]) > val]

    elif '<' in condition:
        col, val = condition.split('<', 1)
        try:
            val = float(val)
        except ValueError:
            raise ValueError(f"Filter value '{val}' for column '{col}' must be a number")
        return [row for row in rows if is_float(row[col], col) and float(row[col]) < val]

    else:
        raise ValueError('Invalid filter condition')
