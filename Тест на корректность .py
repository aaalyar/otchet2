import time
import unittest

class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        rootP = self.find(p)
        rootQ = self.find(q)
        if rootP != rootQ:
            if self.rank[rootP] > self.rank[rootQ]:
                self.parent[rootQ] = rootP
            elif self.rank[rootP] < self.rank[rootQ]:
                self.parent[rootP] = rootQ
            else:
                self.parent[rootQ] = rootP
                self.rank[rootP] += 1

def kruskal(vertices, edges):
    edges.sort(key=lambda x: x[2])
    uf = UnionFind(len(vertices))
    mst = []
    total_cost = 0

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))
            total_cost += weight

    return mst, total_cost

class TestKruskal(unittest.TestCase):
    def run_test_with_timing(self, test_func, test_name):
        print(f"Running {test_name}...")
        start_time = time.time()
        test_func()
        end_time = time.time()
        print(f"Test {test_name} completed in {end_time - start_time:.6f} seconds.\n")

    def test_small_graph(self):
        def inner_test():
            vertices = [0, 1, 2, 3]
            edges = [
                (0, 1, 10),
                (0, 2, 6),
                (0, 3, 5),
                (1, 3, 15),
                (2, 3, 4)
            ]
            expected_mst = [(2, 3, 4), (0, 3, 5), (0, 1, 10)]
            expected_cost = 19
            mst, cost = kruskal(vertices, edges)
            self.assertEqual(sorted(mst), sorted(expected_mst))
            self.assertEqual(cost, expected_cost)
        self.run_test_with_timing(inner_test, "Small Graph")

    def test_dense_graph(self):
        def inner_test():
            vertices = [0, 1, 2, 3]
            edges = [
                (0, 1, 1),
                (0, 2, 1),
                (0, 3, 1),
                (1, 2, 1),
                (1, 3, 1),
                (2, 3, 1)
            ]
            expected_cost = 3
            mst, cost = kruskal(vertices, edges)
            self.assertEqual(len(mst), len(vertices) - 1)
            self.assertEqual(cost, expected_cost)
        self.run_test_with_timing(inner_test, "Dense Graph")

    def test_linear_graph(self):
        def inner_test():
            vertices = [0, 1, 2, 3]
            edges = [
                (0, 1, 5),
                (1, 2, 10),
                (2, 3, 20)
            ]
            expected_mst = [(0, 1, 5), (1, 2, 10), (2, 3, 20)]
            expected_cost = 35
            mst, cost = kruskal(vertices, edges)
            self.assertEqual(sorted(mst), sorted(expected_mst))
            self.assertEqual(cost, expected_cost)
        self.run_test_with_timing(inner_test, "Linear Graph")

    def test_tree_graph(self):
        def inner_test():
            vertices = [0, 1, 2, 3]
            edges = [
                (0, 1, 2),
                (1, 2, 3),
                (2, 3, 4)
            ]
            expected_mst = edges
            expected_cost = 9
            mst, cost = kruskal(vertices, edges)
            self.assertEqual(sorted(mst), sorted(expected_mst))
            self.assertEqual(cost, expected_cost)
        self.run_test_with_timing(inner_test, "Tree Graph")

    def test_disconnected_graph(self):
        def inner_test():
            vertices = [0, 1, 2, 3, 4, 5]
            edges = [
                (0, 1, 1),
                (1, 2, 2),
                (3, 4, 3)
            ]
            expected_mst = [(0, 1, 1), (1, 2, 2), (3, 4, 3)]
            expected_cost = 6
            mst, cost = kruskal(vertices, edges)
            self.assertEqual(sorted(mst), sorted(expected_mst))
            self.assertEqual(cost, expected_cost)
        self.run_test_with_timing(inner_test, "Disconnected Graph")

if __name__ == '__main__':
    unittest.main()
