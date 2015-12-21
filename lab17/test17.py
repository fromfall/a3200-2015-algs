import unittest
import union_find
import kruskal

class TestTopologicalSort(unittest.TestCase):

    def test_dsu(self):
        dsu = union_find.DSU()
        dsu.append()
        dsu.append()
        dsu.append()
        dsu.append()
        dsu.append()
        dsu.unite(0, 3)
        dsu.unite(1, 3)
        self.assertEqual(dsu.find(0), dsu.find(1))
        self.assertNotEqual(dsu.find(0), dsu.find(2))
        dsu.unite(1, 2)
        self.assertEqual(dsu.find(0), dsu.find(2))
        dsu.unite(4, 4)
        dsu.append()
        dsu.unite(4, 5)
        dsu.unite(0, 5)
        for i in range(6):
            self.assertEqual(dsu.find(3), dsu.find(i))

    def test_kruskal(self):
        g = kruskal.WeightedGraph(5)
        g.add_directed_link(0, 1, 0)
        g.add_directed_link(0, 2, 1)
        g.add_directed_link(1, 2, 2)
        g.add_directed_link(2, 3, 3)
        g.add_directed_link(0, 3, 4)
        g.add_directed_link(0, 4, 10)
        t = g.min_tree()
        w = 0
        for edge in t.e:
            w += edge[2]
        self.assertEqual(w, 14)
        self.assertEqual(len(t.e), 4)


if __name__ == '__main__':
    unittest.main()
