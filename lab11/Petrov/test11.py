import unittest
import random
import lab11

class TestSorting(unittest.TestCase):

    def test_trivial(self):
        arr = [1, 333, 22]
        res = lab11.f(arr)
        expected = 0
        self.assertEqual(expected, res)

    def test_empty(self):
        arr = []
        res = lab11.f(arr)
        expected = 0
        self.assertEqual(expected, res)

    def test_moun(self):
        arr = ([1, 10, 0, 0, 0, 11])
        res = lab11.f(arr)
        expected = 30
        self.assertEqual(expected, res)

    def test_std(self):
        arr = [2, 5, 1, 2, 3, 4, 7, 7, 6]
        res = lab11.f(arr)
        expected = 10
        self.assertEqual(expected, res)

    def test_moun1(self):
        arr = [10, 1, 1, 1, 1, 1, 1, 1, 1, 10]
        res = lab11.f(arr)
        expected = 72
        self.assertEqual(expected, res)

if __name__ == '__main__':
    unittest.main()
