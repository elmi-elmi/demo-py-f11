# goal.py

import csv
from collections import namedtuple

file_name1 = './cars.csv'
file_name2 = './personal_info.csv'
files_name = file_name1 + file_name2


def get_dialect(file_name):
    with open(file_name, 'r') as f:
        sample = f.read(1000)
        return csv.Sniffer().sniff(sample=sample)


class FileParser:
    def __init__(self, file_name):
        self._file_name = file_name

    def __enter__(self):
        self._file = open(self._file_name, 'r')
        self._file_reader = csv.reader(self._file, get_dialect(self._file_name))
        header = map(lambda x: x.lower(), next(self._file_reader))
        self._nt = namedtuple('Data', header)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self._file.close()
        return False

    def __iter__(self):
        return self

    def __next__(self):
        if self._file.closed:
            raise StopIteration
        else:
            return self._nt(*next(self._file_reader))


with FileParser(file_name2) as f:
    for row in f:
        print(row)
