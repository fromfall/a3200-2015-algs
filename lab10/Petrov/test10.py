import unittest
import random
from lab10 import f

class TestPythagoras(unittest.TestCase):
    def testmain(self, c):
        B = []
        for i in c:
            if not i in B:
                B.append(i)
                expected = 0
        for i in range(len(B)):
            for j in range(i + 1, len(B)):
                for k in range(j + 1, len(B)):
                    if B[i]**2 + B[j]**2 == B[k]**2:
                        expected += 1
        res = f(B)
        self.assertEqual(res, expected)

    def test_empty(self):
        self.testmain([])

    def test_std(self):
        self.testmain([23, 247, 19, 96, 264, 265, 132, 265, 181])

    def test_duplicates(self):
        self.testmain([3, 4, 3, 3, 5, 4, 1, 1, 1, 4, 5, 3, 4, 2, 2, 2, 5, 5, 4, 3, 2])

    def test_random(self):
        c = [randint(-11111, 11111) for i in range(111)]
        self.testmain(c)
