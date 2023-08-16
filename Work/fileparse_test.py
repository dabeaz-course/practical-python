from fileparse import parse_csv

def test_parse_csv_select_3_4():
    assert parse_csv('Data/portfolio.csv', select=['name','shares']) == \
        [{'name': 'AA', 'shares': '100'}, {'name': 'IBM', 'shares': '50'},
         {'name': 'CAT', 'shares': '150'}, {'name': 'MSFT', 'shares': '200'},
         {'name': 'GE', 'shares': '95'}, {'name': 'MSFT', 'shares': '50'},
         {'name': 'IBM', 'shares': '100'}]
