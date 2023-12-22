#!/usr/bin/python3
"""
log parsing
"""

from collections import defaultdict
import sys


def parse_line(line):
    """
    function that parses the lines
    """
    parts = line.split()
    if len(parts) >= 7 and parts[5].isdigit():
        return {
                'status_code': int(parts[5])
                'file_size': int(parts[6])
                }
        return None


def print_statistics(total_size, status_counts):
    """
    fucntion that prints the statistics
    """
    print(f"Total file size: {total_size}")
    for code in sorted(status_counts.keys()):
        print(f"{code}: {status_counts[code]}")


def process_lines():
    """
    function that processes the lines
    """
    total_size = 0
    status_counts = defaultdict(int)
    lines_processed = 0

    try:
        for line in sys.stdin:
            parsed_line = parse_line(line)
            if parsed_line:
                total_size += parsed_line['file_size']
                status_counts[parsed_line['status_code']] += 1
                lines_processed += 1

                if lines_processed % 10 == 0:
                    print_statistics(total_size, status_counts)
    except KeyboardInterrupt:
        print_statistics(total_size, status_counts)


if __name__ == "__main__":
    process_lines()
