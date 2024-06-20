#!/usr/bin/python3
"""
script that reads stdin line by line and computes metrics
"""
import sys
import signal

total_size = 0
status_counts = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

def print_stats():
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        parts = line.split()
        if len(parts) != 10:
            continue

        ip, dash, date, get, path, http, status, size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[9]

        try:
            status = int(status)
            size = int(size)
        except ValueError:
            continue

        total_size += size
        if status in status_counts:
            status_counts[status] += 1

        line_count += 1
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
