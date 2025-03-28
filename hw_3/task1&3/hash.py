from matrix import Matrix, write_res

class HashMatrixMixin:
    def __hash__(self):
        """
        Делаем xor между всеми элементами
        """
        ans = 0
        for i in self.matrix:
            for j in i:
                ans ^= hash(j)
        return ans

class MatrixWithHash(HashMatrixMixin, Matrix):
    __hash__ = HashMatrixMixin.__hash__

    def __init__(self, matrix):
        super().__init__(matrix)
        self.sl = {}

    @property
    def sl(self):
        return self._sl

    @sl.setter
    def sl(self, value):
        self._sl = value

    def __eq__(self, other):
        return self.matrix == other.matrix

    def __matmul__(self, other):
        if not hash(self) in self.sl:
            self.sl[hash(self)] = {}
        if not hash(other) in self.sl[hash(self)]:
            self.sl[hash(self)][hash(other)] = MatrixWithHash((super().__matmul__(other)).matrix)
        return self.sl[hash(self)][hash(other)]


if __name__ == "__main__":
    A = MatrixWithHash([
        [1, 0],
        [0, 1]
    ])
    C = MatrixWithHash([
        [1, 1],
        [1, 1]
    ])
    B = MatrixWithHash([
        [2, 2],
        [2, 2]
    ])
    D = MatrixWithHash([
        [2, 2],
        [2, 2]
    ])
    assert (hash(A) == hash(C)) and (A != C) and (B == D) and (A @ B != C @ D)
    write_res("./task3/AB.txt", A, B, "@", A @ B)
    write_res("./task3/CD.txt", C, D, "@", C @ D)
    with open("./task3/hash.txt", "w") as f:
        f.write("hash(A@B)=" + str(hash(A@B)) + "\n")
        f.write("hash(C@D)=" + str(hash(C@D)))
