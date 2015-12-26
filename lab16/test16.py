from lab16 import WeightedGraph
import unittest

class TestD(unittest.TestCase):

    def test_ending(self):
        g = WeightedGraph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_vertex(5)
        g.add_vertex(4)
        g.add_direct_link(1, 2, 1)
        g.add_direct_link(1, 3, 3)
        g.add_direct_link(1, 5, 4)
        g.add_direct_link(1, 4, 5)
        g.add_direct_link(2, 3, 1) 
        g.add_direct_link(3, 5, 1)
        g.add_direct_link(5, 4, 1)
        g.add_direct_link(4, 1, 0)
        res = g.paths(1)
        expected = {1: [1], 2: [1, 2], 3: [1, 2, 3], 4: [1, 2, 3, 5, 4], 5: [1, 2, 3, 5]}
        self.assertEqual(res, expected)

    def test_trivial(self):
        g = WeightedGraph()
        g.add_vertex(10)
        g.add_vertex(20)
        g.add_vertex(30)
        g.add_direct_link(10, 20, 100)
        g.add_direct_link(10, 30, 1)
        g.add_direct_link(30, 20, 2)
        res = g.paths(10)
        expected = {10: [10], 20: [10, 30, 20], 30: [10, 30]}
        self.assertEqual(res, expected)

    def test_lecture(self):
        g = WeightedGraph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_vertex(4)
        g.add_vertex(5)
        g.add_direct_link(1, 2, 10)
        g.add_direct_link(1, 5, 5)
        g.add_direct_link(2, 3, 1)
        g.add_direct_link(2, 5, 2)
        g.add_direct_link(3, 4, 4)
        g.add_direct_link(4, 3, 6)
        g.add_direct_link(4, 1, 7)
        g.add_direct_link(5, 4, 2)
        g.add_direct_link(5, 3, 9)
        g.add_direct_link(5, 2, 3)
        res = g.paths(1)
        expected = {1: [1], 2: [1, 5, 2], 3: [1, 5, 2, 3], 4: [1, 5, 4], 5: [1, 5]}
        self.assertEqual(res, expected)

    def test_ending1(self):
        g = WeightedGraph()
        g.add_vertex(1)
        g.add_vertex(2)
        g.add_vertex(3)
        g.add_vertex(5)
        g.add_vertex(4)
        g.add_direct_link(1, 2, 1)
        res = g.paths(1)
        expected = {1: [1], 2: [1, 2], 3: [], 4: [], 5: []}
        self.assertEqual(res, expected)
        
if __name__ == '__main__':
    unittest.main()
