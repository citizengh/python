class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        linestr = ''
        for line in self.matrix:
          linestr += ' '.join([str(i) for i in line]) + '\n'
        return linestr

    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range
        (len(self.matrix[0]))] for i in range(len(self.matrix))])


m1 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
m2 = [[4, 4, 4], [5, 5, 5], [6, 6, 6]]

mat1 = Matrix(m1)
mat2 = Matrix(m2)
print(mat1)

print(mat1+mat2)