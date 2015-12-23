import unittest
from lab15 import LCA

class Tester(unittest.TestCase):

    def test_example(self):    
        n = 9
        root = 3
        g = [[8], [7], [5, 6, 8], [7, 5], [7], [3, 2], [2], [1, 4, 3], [0, 2]]
        lca = LCA(g, root)
        self.assertEqual(lca.lca(1, 8), 3)
        self.assertEqual(lca.lca(6, 2), 2)
        self.assertEqual(lca.lca(2, 6), 2)
        self.assertEqual(lca.lca(1, 4), 7)

    def test_simple(self):    
        n = 10
        root = 1
        g = [[9], [2, 3], [1, 4, 5], [1, 6, 7], [2], [2], [3, 8, 9], [3], [6], [0, 6]]
        lca = LCA(g, root)
        self.assertEqual(lca.lca(8, 9), 6)
        self.assertEqual(lca.lca(6, 7), 3)
        self.assertEqual(lca.lca(3, 2), 1)
        self.assertEqual(lca.lca(8, 7), 3)
        self.assertEqual(lca.lca(6, 9), 6)
        self.assertEqual(lca.lca(4, 5), 2)

    def test_another(self):    
        n = 15
        root = 5
        g = [[13], [3], [3], [1, 2, 4], [3, 9], [6, 9, 10], [5, 7, 8], [6], [6], [4, 5], 
            [5, 11, 12], [10], [10, 13], [0, 12, 14], [13]]
        lca = LCA(g, root)
        self.assertEqual(lca.lca(0, 14), 13)
        self.assertEqual(lca.lca(13, 11), 10)
        self.assertEqual(lca.lca(11, 0), 10)
        self.assertEqual(lca.lca(3, 7), 5)
        self.assertEqual(lca.lca(7, 8), 6)
        self.assertEqual(lca.lca(9, 10), 5)

if __name__ == '__main__':
    unittest.main()
