from typing import Sequence


class TableFormatter:
    def headings(self, headers: Sequence[str]):
        """
        Emit the table headings.
        """
        raise NotImplementedError

    def row(self, row_data: Sequence[str]):
        """
        Emit a single row of table data.
        """
        raise NotImplementedError
