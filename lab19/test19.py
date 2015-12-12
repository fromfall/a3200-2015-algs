import lab19
import unittest

class TestLevi(unittest.TestCase):
    def test_task(self):
        res = lab19.palin("Levenshtien")
        expected = "eve"
        self.assertEqual(expected, res)

    def test_trivial1(self):
        res = lab19.palin("babcad")
        expected = "bab"
        self.assertEqual(expected, res)

    def test_trivial2(self):
        res = lab19.palin("abca")
        expected = "aba"
        self.assertEqual(expected, res)

    def test_random1(self):
        res = lab19.palin("abcsdgsafghjaergfasgsv")
        expected = "sgsafghgfasgs"
        self.assertEqual(expected, res)

    def test_random2(self):
        res = lab19.palin("vnbxcvbsdfhndfhdxfdsfgdszferyesrgssregerg")
        expected = "sdfdfhfdfds"
        self.assertEqual(expected, res)

    def test_random3(self):
        res = lab19.palin("abcddcbadascbsbascd")
        expected = "abcdddcba"
        self.assertEqual(expected, res)
                

if __name__ == '__main__':
    unittest.main()
