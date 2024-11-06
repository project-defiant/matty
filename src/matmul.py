from __future__ import annotations
from numbers import Number


class Matrix:
    def __init__(self, values: list[list[Number]]) -> None:
        """Matrix"""
        assert isinstance(values, list)
        for row in values:
            assert isinstance(row, list)
            for number in row:
                assert isinstance(number, (int, float))
        # ensure that all lists are the same size
        assert len(set(len(row) for row in values)) == 1

        self._values = values
        self.dim = (len(values), len(values[0]))

    def transpose(self) -> Matrix:
        """Get the transposition of the matrix"""
        length = len(self._values[0])
        idx = 0
        new_values = []
        while idx < length:
            new_row = []
            for row in self._values:
                new_row.append(row[idx])
            idx += 1
            new_values.append(new_row)

        self._values = new_values
        return self


    # def __matmul__(self, b: Matrix) -> Matrix:
    #     assert self.dim[0] == b.dim[1], "Number of columns of A must be equal to number of rows in B in A @ B"
    #     for row in 