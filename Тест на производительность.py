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
# Пример использования
if __name__ == "__main__":
    vertices = [0, 1, 2, 3]  # Вершины графа
    edges = [  # Рёбра графа (начальная вершина, конечная вершина, вес)
        (0, 1, 10),
        (0, 2, 6),
        (0, 3, 5),
        (1, 3, 15),
        (2, 3, 4)
    ]
    mst, total_cost = kruskal(vertices, edges)
    print("Кратчайшее связывающее дерево:", mst)
    print("Общая стоимость:", total_cost)

# Тесты
class TestKruskalAlgorithm(unittest.TestCase):
    def test_basic_case(self):
        vertices = [0, 1, 2, 3]
        edges = [
            (0, 1, 10),
            (0, 2, 6),
            (0, 3, 5),
            (1, 3, 15),
            (2, 3, 4)
        ]
        mst, cost = kruskal(vertices, edges)
        expected_cost = 19  # Проверка ожидаемой стоимости минимального остовного дерева
        self.assertEqual(cost, expected_cost)
        self.assertEqual(len(mst), 3)  # Ожидаемое количество рёбер в MST = V - 1

    def test_large_graph_performance(self):
        vertices = list(range(1000))
        edges = [(i, (i + 1) % 1000, i % 100) for i in range(1000)]
        start_time = time.time()
        kruskal(vertices, edges)
        end_time = time.time()
        print(f"Time taken for 1000 vertices: {end_time - start_time:.4f} seconds")

if __name__ == '__main__':
    unittest.main()
