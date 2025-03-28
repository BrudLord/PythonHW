import numpy as np


class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        if isinstance(matrix, np.ndarray):
            self.matrix = matrix.tolist()
        else:
            self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0]) if self.rows > 0 else 0

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise SyntaxError("Matrix can sum only with other Matrix")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix should have same shape")

        return Matrix(
            [[self.matrix[i][j] + other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        )

    def __mul__(self, other):
        if not isinstance(other, Matrix):
            raise SyntaxError("Matrix can mul only with other Matrix")
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Matrix should have same shape")

        return Matrix(
            [[self.matrix[i][j] * other.matrix[i][j] for j in range(self.cols)] for i in range(self.rows)]
        )

    def __matmul__(self, other):
        if not isinstance(other, Matrix):
            raise SyntaxError("Matrix can matmul only with other Matrix")
        if self.cols != other.rows:
            raise ValueError("Right matrix should have same cols as left matrix have rows")
        res = []
        for i in range(self.rows):
            res.append([])
            for j in range(other.cols):
                res[-1].append(sum([self.matrix[i][h] * other.matrix[h][j] for h in range(self.cols)]))
        return Matrix(res)

    def __str__(self):
        return '\n'.join([' '.join(map(str, h)) for h in self.matrix])

def write_res(file: str, A: Matrix, B: Matrix, oper: str, res: Matrix):
    with open(file, "w") as f:
        f.write(str(A))
        f.write(f"\n{oper}\n")
        f.write(str(B))
        f.write("\n=\n")
        f.write(str(res))


if __name__ == "__main__":
    np.random.seed(0)
    X = Matrix(np.random.randint(0, 10, (10, 10)))
    Z = Matrix(np.random.randint(0, 10, (10, 10)))
    write_res("./task1/matrix+.txt", X, Z, "+", X + Z)
    write_res("./task1/matrix_mul.txt", X, Z, "*", X * Z)
    write_res("./task1/matrix@.txt", X, Z, "@", X @ Z)

