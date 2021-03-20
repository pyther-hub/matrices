class Matrix:
    def __init__(self, data_structure):
        self.matrix = data_structure
        self.column_count = len(data_structure[0])
        self.row_count = len(data_structure)
        self.order = [self.row_count, self.column_count]

    def is_square(self):
        if self.row_count == self.column_count:
            return True
        else:
            return False

    def is_indempotent_check(self):
        if multiply(self, self) == self.matrix:
            return True
        else:
            return False

    def is_symmetric(self):
        if self.transpose().matrix == self.matrix:
            return True
        else:
            return False

    def is_skew_symmetric(self):
        print(self.transpose().matrix)
        print(self.scalar_product(-1).matrix)
        if self.transpose().matrix == self.scalar_product(-1).matrix:
            return True
        else:
            return False

    def is_orthogonal(self):
        if self.is_square() == True:
            if multiply(self, self.transpose()).matrix == create_identity_matrix(self.row_count).matrix:
                return True
            else:
                return False
        else:
            raise Exception('NOT COMFORMABLE!! it should be a square matrix')

    def element(self, i, j):
        return self.matrix[i-1][j-1]

    def replace(self, i, j, new):
        self.matrix[i-1][j-1] = new
        return None

    def row(self, m):
        return self.matrix[m-1]

    def column(self, n):
        column = []
        for each_column in self.matrix:
            column.append(each_column[n-1])
        return column

    def transpose(self):
        data_structure = []
        for i in range(0, self.column_count):
            data_structure.append(self.column(i+1))
        return Matrix(data_structure)

    def trace(self):
        if self.square_check() == True:
            value = 0
            for pos in range(0, self.row_count):
                value += self.element(pos, pos)
            return value
        else:
            raise Exception(
                'NOT A SQUARE MATRIX!! this method is for square matrix only')

    def scalar_product(self, k):
        data_structure = self.matrix
        for i in range(0, self.row_count):
            for j in range(0, self.column_count):
                data_structure[i][j] = k*self.element(i+1, j+1)
        return Matrix(data_structure)

    def __str__(self):
        for row in self.matrix:
            print(row)

    def extend_row(self, data):
        if len(data) == self.column_count:
            self.matrix.append(data)
        else:
            raise Exception(
                'column count error!!, length of row is not compatiable with the given matrix')

    def extend_column(self, data):
        if len(data) == self.row_count:
            numb = 0
            for row in self.matrix:
                row.append(data[numb])
                numb += 1
        else:
            raise Exception(
                'row count error!!, length of column is not compatiable with the given matrix')

    def extend_columns(self, data):
        for column in data:
            self.extend_column(column)

    def extend_rows(self, data):
        for row in data:
            self.extend_row(row)

    def delete(self, row=None, column=None):
        data_structure = []
        if row != None:
            for row_pos in range(0, self.row_count):
                if row_pos+1 != row:
                    print('row:-\n', self.row(row_pos+1))
                    data_structure.append(self.row(row_pos+1))
        if column != None:
            for column_pos in range(0, self.transpose().column_count):
                if column_pos+1 != column:
                    print('column:-\n', self.column(column_pos+1))
                    data_structure.append(self.column(column_pos+1))
        print(data_structure)
        return Matrix(data_structure)

    def minor(self, i, j):
        pass


def combine(A, B, sign=1):
    if A.order == B.order:
        data_structure = []
        for i in range(0, A.row_count):
            row = []
            for j in range(0, A.column_count):
                row.append(A.element(i+1, j+1)+B.element(i+1, j+1)*sign)
            data_structure.append(row)
        return Matrix(data_structure)
    else:
        raise Exception(
            'ERROR NOT COMAPATIBLE!! the order of both the matrix is not same')


def multiply(A, B):
    if A.column_count == B.row_count:
        transpose_of_B = B.transpose().matrix
        data_structure = []
        for row in A.matrix:
            row_column = []
            for column in transpose_of_B:
                row_column_array = list(zip(row, column))
                total = 0
                for element_product in row_column_array:
                    total += element_product[0]*element_product[1]
                row_column.append(total)
            data_structure.append(row_column)
        return Matrix(data_structure)
    else:
        raise Exception(
            "NOT CONFORMABLE!! column_count does not match the row_count")


def create_identity_matrix(order):
    data_structure = []
    for i in range(order):
        row = []
        for j in range(order):
            if i == j:
                row.append(1)
            else:
                row.append(0)
        data_structure.append(row)
    return Matrix(data_structure)


a = [1, 2, 3, 4]
b = [1, 4, 9, 16]
A = Matrix([[0, 71, 2], [1, 29, 3], [2, 3, 4]])
B = Matrix([[1, -2], [-1, 0], [2, -1]])
C = Matrix([[22, 3, 90], [81, 64, 121], [1, 8, 17]])
v = Matrix([[22, 3, 90], [81, 64, 121], [1, 8, 17]])
m = Matrix([[0, 1, 2], [1, 2, 3], [2, 3, 4]])
n = Matrix([[1, -2], [-1, 0], [2, -1]])
k = Matrix([[2, -2, -4], [-1, 3, 4], [1, -2, -3]])
sm = Matrix([[0, 2, 3], [-2, 0, 1], [-3, -1, 0]])
p = create_identity_matrix(5)
om = Matrix([[1/3, 2/3, 2/3], [2/3, 1/3, -2/3], [-2/3, 2/3, -1/3]])
print(sm.delete(row=3, column=2).display())
