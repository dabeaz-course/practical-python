# 2.7 Objects
# All objects are first class, everything in python is an object
# Numbers, lists, dictionaries, functions, strings..all can be passed around as data.
# This is what is meant by all objects are first class.



import sys
import csv

def parse_date_slashes(string_data):
    # Takes in a single date represented as a string with '/' for dates.
    # Args: string_data (6/02/2017)
    # Returns: tuple split by '/'

    return tuple(string_data.split('/'))

def read_portfolio(filename):
    """ 
    Read portfolio file (made for dowstocks.csv)
    Args: Filename
    Return: List of dictionaries with key value pairs for each record of this csv file.

    Notes:  This example highlights how functions, str, float are just objects that can be
            represented in a list. (can do something like [math, abs, str, 1, my_function])
            Also shows how you can use list comprehension to piece together a dictionary that 
                * Casts data to proper format.
                * zip together each key value
                * apply function and create dictionary in one go.
    """

    portfolio = []
    with open(filename,'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)

        # In types you can see that we have a user defined functions as part of the
        # set of type conversion functions.

        types = [str, float, parse_date_slashes, str, float, float, float, float, int]
        
        for rowno,row in enumerate(rows):
            try:
                portfolio.append({headers:func(val) for headers,func,val in zip(headers,types,row)})
            except ValueError:
                print(f'Rowno:{rowno} had an error: {row}')

        return portfolio

if len(sys.argv) < 2:
    portfolio = read_portfolio('Data/dowstocks.csv')
else:
    portfolio = read_portfolio(sys.argv[1])

