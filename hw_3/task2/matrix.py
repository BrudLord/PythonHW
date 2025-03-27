import numpy as np
from numpy.lib.mixins import NDArrayOperatorsMixin


class WriteGetSet:
    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, matrix):
        self._matrix = matrix

    @property
    def rows(self):
        return self._rows

    @rows.setter
    def rows(self, value):
        self._rows = value

    @property
    def cols(self):
        return self._cols

    @cols.setter
    def cols(self, value):
        self._cols = value

    def __str__(self):
        return "\n".join(" ".join(map(str, row)) for row in self.matrix)

    def write_to_file(self, file):
        file.write(str(self))


class Matrix(NDArrayOperatorsMixin, WriteGetSet):
    def __init__(self, matrix):
        self.matrix = matrix
        if isinstance(matrix, np.ndarray):
            self.matrix = matrix.tolist()
        else:
            self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    def __array_ufunc__(self, ufunc, method, *inputs, **kwargs):
        mas = []
        for x in inputs:
            if isinstance(x, Matrix):
                mas.append(np.array(x.matrix))
            else:
                mas.append(x)
        result = getattr(ufunc, method)(*mas, **kwargs)
        if isinstance(result, np.ndarray):
            return Matrix(result)
        elif isinstance(result, tuple):
            return tuple(type(self)(x) for x in result)
        else:
            return type(self)(result)


def write_res(file: str, A: Matrix, B: Matrix, oper: str, res: Matrix):
    with open(file, "w") as f:
        A.write_to_file(f)
        f.write(f"\n{oper}\n")
        B.write_to_file(f)
        f.write("\n=\n")
        res.write_to_file(f)


if __name__ == "__main__":
    np.random.seed(0)
    A = Matrix(np.random.randint(0, 10, (10, 10)))
    B = Matrix(np.random.randint(0, 10, (10, 10)))

    write_res("matrix+.txt", A, B, "+", A + B)
    write_res("matrix_mul.txt", A, B, "*", A * B)
    write_res("matrix@.txt", A, B, "@", A @ B)
