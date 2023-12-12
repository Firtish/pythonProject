import csv

fields = []
rows = []

filename = 'records.csv'
with open(filename, 'r') as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter, dialect.quotechar)
    # csvreader = csv.reader(csv_f, delimiter=';')
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)
    print(type(csvreader))  # <class '_csv.reader'>
    csv_f.seek(0)

    fields = next(csvreader)
    for row in csvreader:
        rows.append(row)
    print("Liczba wierszy", csvreader.line_num)

print(fields)
print(rows)
