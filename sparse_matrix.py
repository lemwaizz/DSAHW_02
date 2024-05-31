"""importing relevant libraries"""
import psutil
import sys
import numpy as np
from scipy.sparse import csr_matrix, csc_matrix

class SparseMatrix:
    """class with the sparse matrix functions"""
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
                line = line[1:-1]
                


        