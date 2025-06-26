from typing import List, Dict


def aggregate_column(rows: List[Dict[str, str]], instruction: str) -> Dict[str, str]:
    try:
        col, op = instruction.split('=')
        values = [float(row[col]) for row in rows]
    except Exception as e:
        raise ValueError('Invalid aggregation instruction or non-numeric column') from e

    if op == 'avg':
        result = sum(values) / len(values)
    elif op == 'min':
        result = min(values)
    elif op == 'max':
        result = max(values)
    else:
        raise ValueError('Unsupported aggregation operation')

    return {f'{op}({col})': str(round(result, 2))}
