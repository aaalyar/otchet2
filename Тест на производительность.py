import unittest
import time

# Класс Union-Find
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

# Алгоритм Краскала
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

# Тесты
class TestKruskalAlgorithm(unittest.TestCase):
    def test_basic_case(self):
        start_time = time.time()
        vertices = [0, 1, 2, 3]
        edges = [
            (0, 1, 10),
            (0, 2, 6),
            (0, 3, 5),
            (1, 3, 15),
            (2, 3, 4)
        ]
        mst, cost = kruskal(vertices, edges)
        expected_cost = 19
        self.assertEqual(cost, expected_cost)
        self.assertEqual(len(mst), 3)
        end_time = time.time()
        print(f"Test Basic Case: PASSED in {end_time - start_time:.4f} seconds")

    def test_large_graph_performance(self):
        start_time = time.time()
        vertices = list(range(1000))
        edges = [(i, (i + 1) % 1000, i % 100) for i in range(1000)]
        kruskal(vertices, edges)
        end_time = time.time()
        print(f"Test Large Graph Performance: PASSED in {end_time - start_time:.4f} seconds")

    def test_dense_graph(self):
        start_time = time.time()
        vertices = list(range(50))
        edges = [(i, j, i + j) for i in range(50) for j in range(i + 1, 50)]
        mst, cost = kruskal(vertices, edges)
        self.assertEqual(len(mst), len(vertices) - 1)
        print(f"Cost of MST for Dense Graph: {cost}")
        end_time = time.time()
        print(f"Test Dense Graph: PASSED in {end_time - start_time:.4f} seconds")

    def test_graph_with_negative_weights(self):
        start_time = time.time()
        vertices = [0, 1, 2, 3, 4]
        edges = [
            (0, 1, -1),
            (1, 2, -2),
            (2, 3, -3),
            (3, 4, -4),
            (4, 0, -5)
        ]
        mst, cost = kruskal(vertices, edges)
        self.assertEqual(len(mst), len(vertices) - 1)
        print(f"Cost of MST for Graph with Negative Weights: {cost}")
        end_time = time.time()
        print(f"Test Graph with Negative Weights: PASSED in {end_time - start_time:.4f} seconds")

    def test_disconnected_graph(self):
        start_time = time.time()
        vertices = [0, 1, 2, 3, 4, 5]
        edges = [
            (0, 1, 1),
            (1, 2, 2),
            (3, 4, 3)
        ]
        mst, cost = kruskal(vertices, edges)
        self.assertEqual(len(mst), 3)
        print(f"Cost of MST for Disconnected Graph: {cost}")
        end_time = time.time()
        print(f"Test Disconnected Graph: PASSED in {end_time - start_time:.4f} seconds")

if __name__ == '__main__':
    unittest.main()
