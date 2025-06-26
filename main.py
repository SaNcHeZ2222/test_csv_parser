import argparse
from processor import process_csv
from utils import print_table


def main():
    parser = argparse.ArgumentParser(description='CSV processor')
    parser.add_argument('--file', required=True, help='Path to CSV file')
    parser.add_argument('--where', help='Filter condition, format: column==value | column>value | column<value')
    parser.add_argument('--aggregate', help='Aggregation, format: column=operation (operation: avg, min, max)')
    args = parser.parse_args()

    result = process_csv(args.file, where=args.where, aggregate=args.aggregate)
    print_table(result)


if __name__ == '__main__':
    main()
