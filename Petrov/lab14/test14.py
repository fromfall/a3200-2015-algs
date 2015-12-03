import unittest
import lab14
 
class TestTopologicalSort(unittest.TestCase):
  
    def test_cycle(self):
        graph = lab14.Graph()
        graph.add_vertex(4)
        graph.add_vertex(3)
        graph.add_vertex(2)
        graph.add_vertex(1)
        graph.add_directed_link(2, 3)
        graph.add_directed_link(3, 4)
        graph.add_directed_link(1, 3)
        graph.add_directed_link(4, 2)
        graph.add_directed_link(1, 2)
        res = graph.topological_sort()
        expected = None
        self.assertEquals(expected, res)

    def test_simple(self):
        graph = lab14.Graph()
        graph.add_vertex(4)
        graph.add_vertex(3)
        graph.add_vertex(2)
        graph.add_vertex(1)
        graph.add_directed_link(1, 2)
        graph.add_directed_link(3, 4)
        graph.add_directed_link(2, 3)
        res = graph.topological_sort()
        expected = [1, 2, 3, 4]
        self.assertEquals(expected, res)

    def test_simple1(self):
        graph = lab14.Graph()
        graph.add_vertex(4)
        graph.add_vertex(3)
        graph.add_vertex(2)
        graph.add_vertex(1)
        graph.add_directed_link(4, 2)
        graph.add_directed_link(3, 4)
        graph.add_directed_link(1, 3)
        graph.add_directed_link(1, 2)
        res = graph.topological_sort()
        expected = [1, 3, 4, 2]
        self.assertEquals(expected, res)
 
if __name__ == '__main__':
    unittest.main()
