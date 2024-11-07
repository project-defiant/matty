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
    def test_transpose(self, matrix, transposition):
        m = Matrix(matrix)
        assert isinstance(m, Matrix)
        assert m.transpose()._values == transposition

    @pytest.mark.parametrize(
        ["m", "o", "r"],
        [
            pytest.param([[1, 2, 3]], [[1], [2], [3]], [[14]], id="1 x 3 @ 3 x 1"),
            pytest.param(
                [[1], [2], [3]],
                [[1, 2, 3]],
                [[1, 2, 3], [2, 4, 6], [3, 6, 9]],
                id="3 x 1 @ 1 x 3",
            ),
            pytest.param(
                [[1, 2, 3], [1, 2, 3], [1, 2, 3]],
                [[1, 1, 1], [2, 2, 2], [3, 3, 3]],
                [[14, 14, 14]] * 3,
                id="3 x 3 @ 3 x 3",
            ),
        ],
    )
    def test_matmul(self, m, o, r):
        m = Matrix(m)
        o = Matrix(o)
        s = m @ o
        assert s._values == r
