import unittest
import Grid_Hack

class Test_Grid_Hack(unittest.TestCase):

    def test_init(self):
        matrix = Grid_Hack.init()
        self.assertEqual(len(matrix), Grid_Hack.SIZE)
        for row in matrix:
            self.assertEqual(len(row),Grid_Hack.SIZE)

    def test_sort(self):
        matrix = [[10,5,4], [1,100,20], [1,8,78]]
        cellArray = Grid_Hack.sort(matrix)
        self.assertEqual(cellArray, [(1, 1, 2, 2, 100), (2, 2, 2, 4, 78), (1, 2, 1, 3, 20), (0, 0, 2, 0, 10), (2, 1, 3, 3, 8), (0, 1, 1, 1, 5), (0, 2, 0, 2, 4), (1, 0, 3, 1, 1), (2, 0, 4, 2, 1)])

    def test_createLists(self):
        Grid_Hack.SIZE = 2
        rowArray, colArray, diag1Array, diag2Array = Grid_Hack.createLists()
        self.assertEqual(rowArray, [{'count': 0, 'mul_value': 0, 'cells': [], 'index': 0}, {'count': 0, 'mul_value': 0, 'cells': [], 'index': 1}])
        self.assertEqual(colArray, [{'count': 0, 'mul_value': 0, 'cells': [], 'index': 0}, {'count': 0, 'mul_value': 0, 'cells': [], 'index': 1}])
        self.assertEqual(diag1Array, [{'count': 0, 'mul_value': 0, 'cells': [], 'index': 0}, {'count': 0, 'mul_value': 0, 'cells': [], 'index': 1}, {'count': 0, 'mul_value': 0, 'cells': [], 'index': 2}])
        self.assertEqual(diag2Array, [{'count': 0, 'mul_value': 0, 'cells': [], 'index': 0}, {'count': 0, 'mul_value': 0, 'cells': [], 'index': 1}, {'count': 0, 'mul_value': 0, 'cells': [], 'index': 2}])

    def test_findResult(self):
        matrix = [[60, 25, 53, 61, 14, 71], [54, 19, 19, 25, 59, 70], [69, 45, 72, 27, 19, 19], [6, 38, 47, 90, 42, 56], [0, 58, 56, 96, 85, 14], [72, 41, 100, 26, 83, 91]]
        Grid_Hack.SIZE = len(matrix)
        cellArray = Grid_Hack.sort(matrix)
        rowArray, colArray, diag1Array, diag2Array = Grid_Hack.createLists()
        result = Grid_Hack.findResult(cellArray, rowArray, colArray, diag1Array, diag2Array)
        self.assertEqual(result, {'mul_value': 57970785600L, 'cells': [(5, 2, 8, 7, 100), (5, 5, 5, 10, 91), (5, 4, 6, 9, 83), (5, 0, 10, 5, 72), (5, 1, 9, 6, 41), (5, 3, 7, 8, 26)], 'index': 5, 'label': 'row'}
)

if __name__ == '__main__':
    unittest.main()
