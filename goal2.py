import csv
from collections import namedtuple
from contextlib import contextmanager
from itertools import islice

file_name1 = './cars.csv'
file_name2 = './personal_info.csv'
files_name = file_name1 + file_name2


@contextmanager
def parser_data(file_name):
    file = open(file_name, 'r')

    try:
        dialect = csv.Sniffer().sniff(file.read(1000))
        file.seek(0)
        reader = csv.reader(file, dialect=dialect)
        header = map(lambda x: x.lower(), next(reader))
        nt = namedtuple('Data', header)
        yield (nt(*row) for row in reader)
    finally:
        file.close()


with parser_data(file_name1) as f:
    for row in islice(f, 10):
        print(row)
