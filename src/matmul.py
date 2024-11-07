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

    def __matmul__(self, b: Matrix) -> Matrix:
        assert (
            self.dim[0] == b.dim[1]
        ), "Number of columns of A must be equal to number of rows in B in A @ B"

        def row_x_col(a: list[Number], b: list[Number]):
            return sum(n * m for n, m in zip(a, b))

        j = 0
        result = []
        while j < self.dim[0]:
            left_row = self._values[j]
            k = 0
            while k < b.dim[1]:
                right_col = [c[k] for c in b._values]
                value = row_x_col(left_row, right_col)
                result.append(value)
                k += 1
            j += 1

        dim = (self.dim[0], b.dim[1])
        # reconstruct the Matrix
        values = []
        row = []

        for v in result:
            row.append(v)
            if len(row) == dim[0]:
                values.append(row)
                row = []

        return Matrix(values=values)


    # def strassen_matmul(self, b: Matrix) -> Matrix:
    #     """Calculate the matrix multiplication with Strasen algorithm"""
    #     assert (
    #         self.dim == b.dim 
    #     ), "A and B must be square matrix "

    #     # create an empty matrix of correct size
    #     size = self.dim[0] * b.dim[1]
    #     entry = [0] * size
    #     values = []
    #     row = []
        
    #     for v in entry:
    #         row.append(v)
    #         if len(row) == self.dim[0]:
    #             values.append(row)
    #             row = []

    #     for i in range(0, b.dim[1]):
    #         for j in range(0, )

