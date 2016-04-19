
import csv

def validate_entries(entries, expected_len):
    for entry in entries:
        assert len(entry) == expected_len

def parse(csv_file):
    with open(csv_file) as csv_fd:
        csv_reader = csv.reader(csv_fd, delimiter=',', quotechar='"')
        lines = map(lambda x: x, csv_reader)

    header_cells, entries = lines[0], lines[1:]
    validate_entries(entries, len(header_cells))

    return (header_cells, entries)
