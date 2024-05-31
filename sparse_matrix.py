"""importing relevant libraries"""
import psutil
import sys
import numpy as np
from scipy.sparse import csr_matrix, csc_matrix

class SparseMatrix:
    """class with the sparse matrix functions"""
    def __init__(self, matrixFilePath=None, numRows=None, numCols=None):
        self.matrix = {}
        self.numRows = numRows
        self.numCols = numCols
        if matrixFilePath:
            self.read_from_file(matrixFilePath)

    def setElement(self, row, col, value):
        """setting unique elements in the matrix"""
        if value != 0:
            self.matrix[row, col] = value
        elif (row, col) in self.matrix:
            del self.matrix[row, col]

    def readfromfile(self, matrixFilePath):
        """function to set conditions for the data to be extracted from the files."""
        try:
            with open(matrixFilePath, 'r') as f:
                lines = f.readlines()
            """strip leading and trailing whitespace then access the first and second line and the second element"""
            self.numRows = int(lines[0].strip().split("=")[1])
            self.numCols = int(lines[1].strip().split("=")[1])

            for line in lines[2:]:
                line = line.strip()
                if line == '':
                    continue
                if not (line.startswith("(") and line.endswith(")")):
                    raise ValueError("the line is not the correct format.")
                stripped_line = line[1:-1]
                row, col, value = map(int, stripped_line.split(","))
                self.setElement(row, col, val)
        except ValueError:
            pass





        