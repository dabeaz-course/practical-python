from fileparse import parse_csv


def test_parse_csv_select_3_4():
    assert parse_csv("Data/portfolio.csv", select=["name", "shares"]) == [
        {"name": "AA", "shares": "100"},
        {"name": "IBM", "shares": "50"},
        {"name": "CAT", "shares": "150"},
        {"name": "MSFT", "shares": "200"},
        {"name": "GE", "shares": "95"},
        {"name": "MSFT", "shares": "50"},
        {"name": "IBM", "shares": "100"},
    ]


def test_parse_csv_select_3_5():
    assert parse_csv("Data/portfolio.csv", types=[str, int, float]) == [
        {"price": 32.2, "name": "AA", "shares": 100},
        {"price": 91.1, "name": "IBM", "shares": 50},
        {"price": 83.44, "name": "CAT", "shares": 150},
        {"price": 51.23, "name": "MSFT", "shares": 200},
        {"price": 40.37, "name": "GE", "shares": 95},
        {"price": 65.1, "name": "MSFT", "shares": 50},
        {"price": 70.44, "name": "IBM", "shares": 100},
    ]

    assert parse_csv(
        "Data/portfolio.csv", select=["name", "shares"], types=[str, int]
    ) == [
        {"name": "AA", "shares": 100},
        {"name": "IBM", "shares": 50},
        {"name": "CAT", "shares": 150},
        {"name": "MSFT", "shares": 200},
        {"name": "GE", "shares": 95},
        {"name": "MSFT", "shares": 50},
        {"name": "IBM", "shares": 100},
    ]
