import lab18
import unittest

class TestLevi(unittest.TestCase):
    def test_task(self):
        res = lab18.dl("Levenshtien", "Frankenstein")
        expected = 7
        self.assertEqual(expected, res)

    def test_trivial1(self):
        res = lab18.dl("one", "two")
        expected = 3
        self.assertEqual(expected, res)

    def test_trivial2(self):
        res = lab18.dl("1", "2111")
        expected = 3
        self.assertEqual(expected, res)

    def test_clear(self):
        s1 = ""
        s2 = "here's nothing interesting"
        res = lab18.dl(s1, s2)
        expected = 26
        self.assertEqual(expected, res)

    def test_hard(self):
        s1 = "we will never be in Seattle anywhere and do not get tired to complain about this"
        s2 = "morning evening Learn to be blind forever introverts with sets of contradictions"
        res = lab18.dl(s1, s2)
        expected = 62
        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()
