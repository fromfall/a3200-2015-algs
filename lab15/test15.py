import unittest
from lab15 import LCA

class Tester(unittest.TestCase):

    def test_example(self):    
        n = 9
        root = 3
        v = [[1, 7], [4, 7], [7, 3], [5, 3], [2, 5], [6, 2], [8, 2], [0, 8]]
        g = LCA.list_of_edges(n, v)
        lca = LCA(g, root)
        self.assertEqual(lca.lca(1, 8), 3)
        self.assertEqual(lca.lca(6, 2), 2)
        self.assertEqual(lca.lca(2, 6), 2)
        self.assertEqual(lca.lca(1, 4), 7)

    def test_simple(self):    
        n = 10
        root = 1
        v = [[1, 2], [1, 3], [2, 4], [2, 5], [3, 6], [3, 7], [6, 8], [6, 9], [9, 0]]
        g = LCA.list_of_edges(n, v)
        lca = LCA(g, root)
        self.assertEqual(lca.lca(0, 7), 3)
        self.assertEqual(lca.lca(5, 3), 1)
        self.assertEqual(lca.lca(7, 3), 3)
        self.assertEqual(lca.lca(8, 0), 6)
        self.assertEqual(lca.lca(9, 6), 6)

    def test_another(self):    
        n = 15
        root = 5
        v = [[5, 6], [5, 9], [5, 10], [6, 7], [6, 8], [9, 4], [4, 3], [3, 2], [3, 1],
                    [10, 11], [10, 12], [12, 13], [13, 14], [13, 0]]
        g = LCA.list_of_edges(n, v)
        lca = LCA(g, root)
        self.assertEqual(lca.lca(3, 4), 4)
        self.assertEqual(lca.lca(14, 0), 13)
        self.assertEqual(lca.lca(11, 10), 10)
        self.assertEqual(lca.lca(2, 3), 3)
        self.assertEqual(lca.lca(11, 13), 10)
        self.assertEqual(lca.lca(0, 11), 10)
           

if __name__ == '__main__':
    unittest.main()
