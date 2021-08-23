# tableformat.py

class TableFormatter(object):

	def __init__(self, headers=None):
		self.headers = headers

	def headings(self, headers):
		'''
		Emit table headings
		'''
		raise NotImplementedError()

	def row(self, rowdata):
		'''
		Emit single row of data
		'''
		raise NotImplementedError()


class TextTableFormatter(TableFormatter):

	def headings(self, headers):
		for h in headers:
			print(f'{h:>10s}', end=' ')
		print()
		print(f'{"":->10s} '*len(headers))

	def row(self, rowdata):
		for d in rowdata:
			print(f'{d:>10s}', end=' ')
		print()


class CSVTableFormatter(TableFormatter):
    '''
    Output portfolio data in CSV format.
    '''

    def headings(self, headers):
        print(','.join(headers))

    def row(self, rowdata):
        print(','.join(rowdata))


class HTMLTableFormatter(TableFormatter):
	'''
	Output portfolio data in HTML format.
	'''

	def headings(self, headers):
		temp_string = ''
		for h in headers:
			temp_string += f'<th>{h}</th>'
		print(f'<tr>{temp_string}</tr>')

	def row(self, rowdata):
		temp_string = ''
		for r in rowdata:
			temp_string += f'<td>{r}</td>'
		print(f'<tr>{temp_string}</tr>')


def create_formatter(fmt):
	if fmt == 'txt':
		formatter = TextTableFormatter()
	elif fmt == 'csv':
		formatter = CSVTableFormatter()
	elif fmt == 'html':
		formatter = HTMLTableFormatter()
	else:
		raise RuntimeError(f'Unknown format {fmt}')

	return formatter