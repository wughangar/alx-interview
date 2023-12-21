#!/usr/bin/python3
"""
log parsing
"""

from collections import defaultdict
import sys


def print_statistics(total_size, status_count):
    print(f"Total file size: {total_size}")
    for code in sorted(status_count.keys()):
        print(f"{code}: {status_count[code]}")


def parse_line(line):
    parts = line.split()
    if len(parts) >= 9:
        status_code = parts[8]
        if status_code.isdigit():
            return int(status_code), int(parts[9])
        return None, None


def main():
    total_size = 0
    status_count = defaultdict(int)
    line_count = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            code, size = parse_line(line)
            if code is not None and size is not None:
                total_size += size
                status_count[code] += 1
                line_count += 1
            if line_count == 10:
                print_statistics(total_size, status_count)
                line_count = 0
    except KeyboardInterrupt:
        print_statistics(total_size, status_count)


if __name__ == "__main__":
    main()
