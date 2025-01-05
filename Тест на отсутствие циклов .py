import unittest
import time

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
    def test_cycle_graph(self):
        start_time = time.time()
        vertices = [0, 1, 2, 3, 4]
        edges = [
            (0, 1, 2), (1, 2, 3), (2, 3, 4), 
            (3, 4, 5), (4, 0, 6)
        ]
        expected_mst = [(0, 1, 2), (1, 2, 3), (2, 3, 4), (3, 4, 5)]
        mst, cost = kruskal(vertices, edges)
        self.assertEqual(sorted(mst), sorted(expected_mst))
        self.assertEqual(cost, 14)
        print(f"test_cycle_graph completed in {time.time() - start_time:.6f} seconds")

    def test_large_graph(self):
        start_time = time.time()
        vertices = list(range(10))
        edges = [(i, i + 1, i + 1) for i in range(9)] + [(0, 9, 50)]
        mst, cost = kruskal(vertices, edges)
        self.assertEqual(len(mst), len(vertices) - 1)
        self.assertEqual(cost, 45)
        print(f"test_large_graph completed in {time.time() - start_time:.6f} seconds")

    def test_disconnected_components(self):
        start_time = time.time()
        vertices = [0, 1, 2, 3, 4, 5]
        edges = [(0, 1, 3), (2, 3, 1), (4, 5, 2)]
        expected_mst = edges
        mst, cost = kruskal(vertices, edges)
        self.assertEqual(sorted(mst), sorted(expected_mst))
        self.assertEqual(cost, 6)
        print(f"test_disconnected_components completed in {time.time() - start_time:.6f} seconds")

    def test_negative_weights(self):
        start_time = time.time()
        vertices = [0, 1, 2, 3]
        edges = [
            (0, 1, -10), (1, 2, -5), (2, 3, 0), 
            (3, 0, -1), (0, 2, 2)
        ]
        expected_mst = [(0, 1, -10), (1, 2, -5), (3, 0, -1)]
        expected_cost = -16
        mst, cost = kruskal(vertices, edges)
        self.assertEqual(sorted(mst), sorted(expected_mst))
        self.assertEqual(cost, expected_cost)
        print(f"test_negative_weights completed in {time.time() - start_time:.6f} seconds")

if __name__ == "__main__":
    unittest.main()
