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

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):
            uf.union(u, v)
            mst.append((u, v, weight))

    return mst


class TestKruskalAlgorithm(unittest.TestCase):
    def test_single_vertex_no_edges(self):
        start_time = time.time()  # Засекаем время
        vertices = [0]
        edges = []
        mst = kruskal(vertices, edges)
        print(f"Test 'Single Vertex No Edges': MST = {mst}")
        self.assertEqual(mst, [])
        end_time = time.time()  # Засекаем время после выполнения
        print(f"Test 'Single Vertex No Edges' execution time: {end_time - start_time:.6f} seconds")

    def test_same_weight_edges(self):
        start_time = time.time()
        vertices = [0, 1, 2, 3]
        edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1)]
        mst = kruskal(vertices, edges)
        print(f"Test 'Same Weight Edges': MST = {mst}")
        self.assertEqual(len(mst), 3)  # Для 4 вершин (V-1 рёбер)
        end_time = time.time()
        print(f"Test 'Same Weight Edges' execution time: {end_time - start_time:.6f} seconds")

    def test_disconnected_graph(self):
        start_time = time.time()
        vertices = [0, 1, 2, 3, 4, 5]
        edges = [(0, 1, 2), (1, 2, 3), (3, 4, 4)]
        mst = kruskal(vertices, edges)
        print(f"Test 'Disconnected Graph': MST = {mst}")
        self.assertEqual(len(mst), 3)
        end_time = time.time()
        print(f"Test 'Disconnected Graph' execution time: {end_time - start_time:.6f} seconds")

    def test_large_graph(self):
        start_time = time.time()
        vertices = list(range(10))
        edges = [(i, (i + 1) % 10, 1) for i in range(10)]
        mst = kruskal(vertices, edges)
        print(f"Test 'Large Graph': MST = {mst}")
        self.assertEqual(len(mst), 9)
        end_time = time.time()
        print(f"Test 'Large Graph' execution time: {end_time - start_time:.6f} seconds")

    def test_negative_weights(self):
        start_time = time.time()
        vertices = [0, 1, 2, 3]
        edges = [(0, 1, -2), (1, 2, -3), (2, 3, -1), (0, 3, 4)]
        mst = kruskal(vertices, edges)
        print(f"Test 'Negative Weights': MST = {mst}")
        self.assertEqual(len(mst), 3)
        end_time = time.time()
        print(f"Test 'Negative Weights' execution time: {end_time - start_time:.6f} seconds")

    # Пограничные случаи

    def test_graph_with_one_edge(self):
        start_time = time.time()
        vertices = [0, 1]
        edges = [(0, 1, 5)]  # Одно ребро с весом 5
        mst = kruskal(vertices, edges)
        print(f"Test 'Graph with One Edge': MST = {mst}")
        self.assertEqual(mst, [(0, 1, 5)])
        end_time = time.time()
        print(f"Test 'Graph with One Edge' execution time: {end_time - start_time:.6f} seconds")

    def test_graph_with_same_weight_edges(self):
        start_time = time.time()
        vertices = [0, 1, 2]
        edges = [(0, 1, 3), (1, 2, 3), (0, 2, 3)]  # Все рёбра одинакового веса
        mst = kruskal(vertices, edges)
        print(f"Test 'Graph with Same Weight Edges': MST = {mst}")
        self.assertEqual(len(mst), 2)  # Два ребра из трёх, образуют минимальное дерево
        end_time = time.time()
        print(f"Test 'Graph with Same Weight Edges' execution time: {end_time - start_time:.6f} seconds")

    def test_empty_graph(self):
        start_time = time.time()
        vertices = []
        edges = []
        mst = kruskal(vertices, edges)
        print(f"Test 'Empty Graph': MST = {mst}")
        self.assertEqual(mst, [])
        end_time = time.time()
        print(f"Test 'Empty Graph' execution time: {end_time - start_time:.6f} seconds")

if __name__ == '__main__':
    unittest.main()
