import goal1

with open(goal1.file_name1) as f:
    for row in list(f)[0:3]:
        print([row])

print('=======================')

with open(goal1.file_name2) as f:
    for row in list(f)[0:3]:
        print([row])
print('')

import csv

with open(goal1.file_name1) as f:
    sample = f.read(2000)
    dialect = csv.Sniffer().sniff(sample)

print(vars(dialect))
print('======')
with open(goal1.file_name1) as f:
    reader = csv.reader(f, dialect)
    for row in list(reader)[0:5]:
        print(row)
