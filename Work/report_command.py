from os import path
from report import make_report_2_9

data_dir = path.join(path.dirname(__file__), 'Data')

make_report_2_9(
    path.join(data_dir, 'portfolio.csv'),
    path.join(data_dir, 'prices.csv'))