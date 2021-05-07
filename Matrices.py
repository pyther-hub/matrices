import time
from fractions import Fraction
import random


class Matrix:
    def __init__(self, matrix):
        self.row_count = len(matrix)
        self.column_count = len(matrix[0])
        self.order = [self.row_count, self.column_count]
        self.matrix = matrix

    def __str__(self) -> str:
        self.display_matrix()
        return None

    def is_square(self):
        return self.row_count == self.column_count

    def is_indempotent(self):
        return multiply(self, self) == self.matrix

    def is_symmetric(self):
        return self.transpose().matrix == self.matrix

    def is_skew_symmetric(self):
        return self.transpose().matrix == self.scalar_product(-1).matrix

    def is_orthogonal(self) -> bool:
        if self.is_square() and multiply(self, self.transpose()).matrix == create_identity_matrix(self.row_count).matrix:
            return True
        if self.is_square():
            return False
        raise Exception('NOT COMFORMABLE!! it should be a square matrix')

    def element(self, i: int, j: int) -> int:
        return self.matrix[i-1][j-1]

    def replace(self, i: int, j: int, new: int) -> None:
        self.matrix[i-1][j-1] = new
        return None

    def row(self, m: int) -> list:
        return self.matrix[m-1]

    def column(self, n: int) -> list:
        return [row[n-1] for row in self.matrix]

    def transpose(self):
        data_structure = list(zip(*self.matrix))
        return Matrix(data_structure)

    def trace(self):
        if not self.is_square():
            raise Exception(
                'NOT A SQUARE MATRIX!! this method is for square matrix only')
        return sum([self.element(pos+1, pos+1) for pos in range(self.row)])

    def scalar_product(self, k: int):
        data_structure = self.matrix
        for i in range(0, self.row_count):
            for j in range(0, self.column_count):
                data_structure[i][j] = k*self.element(i+1, j+1)
        return ResultantMatrix(data_structure)

    def display_matrix(self):
        for row in self.matrix:
            print(row)
        return None

    def extend_row(self, data: list):
        if len(data) == self.column_count:
            self.matrix.append(data)
        else:
            raise Exception(
                'column count error!!, length of row is not compatiable with the given matrix')

    def extend_column(self, data: list):
        if len(data) == self.row_count:
            numb = 0
            for row in self.matrix:
                row.append(data[numb])
                numb += 1
        else:
            raise Exception(
                'row count error!!, length of column is not compatiable with the given matrix')

    def extend_columns(self, data: list):
        for column in data:
            self.extend_column(column)

    def extend_rows(self, data: list):
        for row in data:
            self.extend_row(row)

    def copy(self):
        data_structure = []
        for row in self.matrix:
            data_structure.append(row.copy())
        return Matrix(data_structure)

    def delete(self, row=None, column=None):
        minor_matrix = self.copy().matrix
        if row is not None:
            del minor_matrix[row - 1]
        if column is not None:
            for each_column in minor_matrix:
                del each_column[column - 1]
        return Matrix(minor_matrix)

    def adjoint(self):
        if self.is_square():
            adjoint_matrix = Matrix([[(-1)**(r+c)*self.delete(r+1, c+1).determinant()
                                    for r in range(self.row_count)] for c in range(self.column_count)])
            return adjoint_matrix

    def determinant(self) -> int:
        if not self.is_square():
            raise Exception('ONLY SQUARE MATRIX IS ALLOWED')

        if self.order == [2, 2]:
            det = self.matrix
            return det[0][0]*det[1][1]-det[0][1]*det[1][0]

        top_row = self.row(1)
        minor_matrix = self.delete(row=1)
        position = 0
        answer = 0
        sign = +1
        for element in top_row:
            coeff = (minor_matrix.delete(
                column=position+1)).determinant()
            answer += sign*element * coeff
            sign *= -1
            position += 1
        return answer

    def inverse(self):
        return self.adjoint().scalar_product(1/self.determinant())


class ResultantMatrix(Matrix):
    def __init__(self, data_structure):
        self.matrix = data_structure
        self.row_count = len(data_structure)
        self.column_count = len(data_structure[0])
        self.order = [self.row_count, self.column_count]


def combine(A: Matrix, B: Matrix, sign: int):
    if A.order == B.order:
        data_structure = [[A.element(i+1, j+1)+sign*B.element(i+1, j+1)
                           for i in range(A.row_count)] for j in range(A.column_count)]
        return Matrix(data_structure)
    raise Exception(
        'ERROR NOT COMAPATIBLE!! the order of both the matrix is not same')


def multiply(A: Matrix, B: Matrix):
    transpose_of_B = B.transpose().matrix
    product_matrix = Matrix([[sum(map(lambda x, y: x*y, row, column))
                            for column in transpose_of_B] for row in A.matrix])
    return product_matrix


def create_identity_matrix(order: int) -> ResultantMatrix:
    return ResultantMatrix([[1 if i == j else 0 for i in range(order)] for j in range(order)])


def create_random_matrix(row: int, column: int, scale: list):
    data_structure = [[random.randrange(scale[0], scale[1])
                       for i in range(row)]for j in range(column)]
    return Matrix(data_structure)


A = create_random_matrix(5, 5, [-60, 60])
B = create_random_matrix(5, 5, [-60, 60])
A = Matrix([[38, -52, 55, 2, 28],
            [2, 30, -46, -30, 4],
            [40, -48, 18, 20, -43],
            [-17, -48, -60, -38, 57],
            [-58, -40, 59, -4, 9]])
print('\n'*4)
print(A.adjoint())
