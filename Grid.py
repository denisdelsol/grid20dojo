import random

SIZE = 20
MAX_INT = 100
NUMBER_OF_CELLS = 4

def init():
    """Fill a matrix with random integers"""
    matrix = []
    for i in range(SIZE):
        row = []
        for j in range(SIZE):
            n = random.randint(0,MAX_INT)
            row.append(n)
        matrix.append(row)
    return matrix

def sort(matrix):
    """"Create a list of all the cells with their coordinates and sort those cells based on their values"""
    cellArray = []

    rowIndex = 0
    size = len(matrix)
    for row in matrix:
        colIndex = 0
        for col in row:
            #(row, colum, diag1, diag2, value)
            cellArray.append((rowIndex, colIndex, rowIndex-colIndex+size-1, rowIndex+colIndex, col))
            colIndex += 1
        rowIndex += 1
    return sorted(cellArray, key=lambda tup: tup[4], reverse=True)

def createLists():
    """Create empty lists to store the rows, columns and the two diagonals of the matrix """
    rowArray = []
    colArray = []
    diag1Array = []
    diag2Array = []
    for i in range(SIZE):
        rowArray.append({"mul_value":0, "count":0, "index":i, "cells":[]})
        colArray.append({"mul_value":0, "count":0, "index":i, "cells":[]})
    for j in range(2*SIZE-1):
        diag1Array.append({"mul_value":0, "count":0, "index":j, "cells":[]})
        diag2Array.append({"mul_value":0, "count":0, "index":j, "cells":[]})

    return rowArray, colArray, diag1Array, diag2Array

def action(line_tuple, cell):
    """Add a cell to its own row, column or diagonal"""
    if line_tuple["count"] == 0:
        line_tuple["mul_value"] = cell[4]
        line_tuple["cells"].append(cell)
    elif line_tuple["count"] == NUMBER_OF_CELLS-1:
        line_tuple["mul_value"] = line_tuple["mul_value"] * cell[4]
        line_tuple["cells"].append(cell)
        return True
    elif line_tuple["count"] >= NUMBER_OF_CELLS:
        return False
    else:
        line_tuple["mul_value"] = line_tuple["mul_value"] * cell[4]
        line_tuple["cells"].append(cell)
    line_tuple["count"] += 1
    return False

def findResult(sortedList, rowArray, colArray, diag1Array, diag2Array):
    result = {"mul_value": 0, "label": "row", "index": 0, "cells": []}
    for cell in sortedList:
        #print cell
        if action(rowArray[cell[0]], cell) and rowArray[cell[0]]["mul_value"] > result["mul_value"]:
            result = {"mul_value": rowArray[cell[0]]["mul_value"], "label": "row", "index": cell[0], "cells": rowArray[cell[0]]["cells"]}
        if action(colArray[cell[1]], cell) and colArray[cell[1]]["mul_value"] > result["mul_value"]:
            result = {"mul_value": colArray[cell[1]]["mul_value"], "label": "col", "index": cell[1], "cells": colArray[cell[1]]["cells"]}
        if action(diag1Array[cell[2]], cell) and diag1Array[cell[2]]["mul_value"] > result["mul_value"]:
            result = {"mul_value": diag1Array[cell[2]]["mul_value"], "label": "diag1", "index": cell[2], "cells": diag1Array[cell[3]]["cells"]}
        if action(diag2Array[cell[3]], cell) and diag2Array[cell[3]]["mul_value"] > result["mul_value"]:
            result = {"mul_value": diag2Array[cell[3]]["mul_value"], "label": "diag2", "index": cell[3], "cells": diag2Array[cell[3]]["cells"]}
    return result

def main():
    matrix = init()
    print matrix
    sortedList = sort(matrix)
    rowArray, colArray, diag1Array, diag2Array = createLists()
    result = findResult(sortedList, rowArray, colArray, diag1Array, diag2Array)
    print "Max found on", result["label"], result["index"], "with product", result["mul_value"], "and cells", result["cells"]

if __name__ == "__main__":
    main()
