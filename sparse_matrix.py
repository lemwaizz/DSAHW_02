# Importing relevant libraries
import numpy as np
from scipy.sparse import csr_matrix, csc_matrix

class SparseMatrix:
    """Class with the sparse matrix functions"""
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        self.matrix = {}
        self.numRows = numRows
        self.numCols = numCols
        if matrixFilePath:
            self.read_from_file(matrixFilePath)

    def setElement(self, currRow, currCol, value):
        """Setting unique elements in the matrix"""
        if value != 0:
            self.matrix[currRow, currCol] = value
        elif (currRow, currCol) in self.matrix:
            del self.matrix[currRow, currCol]

    def read_from_file(self, matrixFilePath):
        """Function to read matrix data from a file"""
        try:
            with open(matrixFilePath, 'r') as f:
                lines = f.readlines()
            # Strip leading and trailing whitespace then access the first and second lines
            self.numRows = int(lines[0].strip().split("=")[1])
            self.numCols = int(lines[1].strip().split("=")[1])

            for line in lines[2:]:
                line = line.strip()
                if line == '':
                    continue
                if not (line.startswith("(") and line.endswith(")")):
                    raise ValueError("Input file has wrong format")
                stripped_line = line[1:-1]
                row, col, value = map(int, stripped_line.split(","))
                self.setElement(row, col, value)
        except ValueError as e:
            print(f"Error: {e}")
            raise

    def getElement(self, currRow, currCol):
        return self.matrix.get((currRow, currCol), 0)

    def __add__(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must be equal")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for (i, j), v in self.matrix.items():
            result.setElement(i, j, v)
        for (i, j), v in other.matrix.items():
            result.setElement(i, j, result.getElement(i, j) + v)
        return result

    def __sub__(self, other):
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must agree")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        for (i, j), v in self.matrix.items():
            result.setElement(i, j, v)
        for (i, j), v in other.matrix.items():
            result.setElement(i, j, result.getElement(i, j) - v)
        return result

    def __mul__(self, other):
        if self.numCols != other.numRows:
            raise ValueError("Matrix dimensions do not allow multiplication")
        result = SparseMatrix(numRows=self.numRows, numCols=other.numCols)
        for (i, k), v in self.matrix.items():
            for j in range(other.numCols):
                if (k, j) in other.matrix:
                    result.setElement(i, j, result.getElement(i, j) + v * other.matrix[(k, j)])
        return result

    def __str__(self):
        elements = [f"{key}: {value}" for key, value in self.matrix.items()]
        return "\n".join(elements)

if __name__ == "__main__":
    matrix1 = SparseMatrix("drive-download-20240531T112323Z-001/easy_sample_02_1.txt")
    matrix2 = SparseMatrix("drive-download-20240531T112323Z-001/easy_sample_02_2.txt")

    sum_matrix = matrix1 + matrix2
    print("Addition Result:")
    print(sum_matrix)

    diff_matrix = matrix1 - matrix2
    print("Subtraction Result:")
    print(diff_matrix)

    try:
        prod_matrix = matrix1 * matrix2
        print("Multiplication Result:")
        print(prod_matrix)
    except ValueError as e:
        print(f"Multiplication Error: {e}")
