import csv

def read_dowstocks(filename):
    f = open(filename)
    rows = csv.reader(f)
    header = next(rows)
    row = next(rows)
    types = [str, float, tuple, str, float, float, float, float, int]

    converted = { name: func(val) for name,func, val in (zip(header,types,row)) if func}

    print(converted)