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

class TestKruskalAlgorithm(unittest.TestCase):
    def test_single_vertex_no_edges(self):
        vertices = [0]
        edges = []
        mst, cost = kruskal(vertices, edges)
        self.assertEqual(mst, [])
        self.assertEqual(cost, 0)
    def test_same_weight_edges(self):
        vertices = [0, 1, 2, 3]
        edges = [(0, 1, 1), (1, 2, 1), (2, 3, 1), (3, 0, 1)]
        mst, cost = kruskal(vertices, edges)
        self.assertEqual(cost, 3)


if __name__ == '__main__':
    unittest.main()
