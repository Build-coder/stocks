import csv

with open('stocks.csv') as _file:
    csv_reader = csv.reader(_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]}, {row[1]}, {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')
