import lab20
import unittest

class TestLevi(unittest.TestCase):

    def test_std1(self):
        n = 4
        m = [2, 4, 4, 2]
        res = lab20.solve(n, m)
        expected = 8
        self.assertEqual(expected, res)

    def test_std2(self):
        n = 4
        m = [2, 2, 3, 5]
        res = lab20.solve(n, m)
        expected = 0
        self.assertEqual(expected, res)

    def test_std3(self):
        n = 4
        m = [100003, 100004, 100005, 100006]
        res = lab20.solve(n, m)
        expected = 10000800015
        self.assertEqual(expected, res)

    def test_medium(self):
        n = 8
        m = [10, 10, 10, 10, 11, 10, 11, 10]
        res = lab20.solve(n, m)
        expected = 210
        self.assertEqual(expected, res)

    def test_medium2(self):
        n = 20
        m = [4, 4, 8, 4, 5, 6, 7, 4, 5, 4, 6, 4, 4, 5, 7, 6, 5, 8, 8, 4]
        res = lab20.solve(n, m)
        expected = 149
        self.assertEqual(expected, res)

    def test_hard(self):
        n = 10
        m = [10519, 10519, 10520, 10520, 10520, 10521, 10521, 10521, 10522, 10523]
        res = lab20.solve(n, m)
        expected = 221372362
        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()
