import pytest


from matmul import Matrix


class TestMatrix:

    @pytest.mark.parametrize(
        ["matrix", "dim"],
        [
            pytest.param([[1, 2, 3]], (1, 3), id="1 x 3"),
            pytest.param([[1, 2, 3], [4, 5, 6]], (2, 3), id="2 x 3"),
        ],
    )
    def test_constructor(self, matrix, dim):
        m = Matrix(matrix)
        assert isinstance(m, Matrix)
        assert m.dim == dim

    @pytest.mark.parametrize(
        ["matrix", "transposition"],
        [
            pytest.param([[1, 2, 3]], [[1], [2], [3]], id="1 x 3"),
            pytest.param([[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]], id="2 x 3"),
        ],
    )
    def test_constructor(self, matrix, transposition):
        m = Matrix(matrix)
        assert isinstance(m, Matrix)
        assert m.transpose()._values == transposition
