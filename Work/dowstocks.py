import csv

def date_tuple(s):
    return tuple(str(s).split('/'))

def main():
    with open('Data/dowstocks.csv') as f:
        rows = csv.reader(f)
        headers = next(rows)
        print(headers)
        types = [str, float, date_tuple, str, float, float, float, float, int]
        dow_stocks = [
            { key: func(val) for key, func, val in zip(headers, types, row) }
            for row in rows
        ]
        print(dow_stocks[0]['date'])
        print(len(dow_stocks))

if __name__ == '__main__':
    main()