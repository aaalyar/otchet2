class UnionFind:
    def __init__(self, size):
        # Инициализация массива родительских вершин и рангов
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, p):
        # Поиск корня компоненты с компрессией путей
        if self.parent[p] != p:
            self.parent[p] = self.find(self.parent[p])
        return self.parent[p]

    def union(self, p, q):
        # Объединение двух компонентов по рангу
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
    # Сортируем рёбра по весу
    edges.sort(key=lambda x: x[2])  
    uf = UnionFind(len(vertices))  # Инициализация Union-Find
    mst = []  # Список для хранения рёбер минимального остовного дерева
    total_cost = 0  # Общая стоимость остовного дерева

    for u, v, weight in edges:
        if uf.find(u) != uf.find(v):  # Проверка на циклы
            uf.union(u, v)  # Объединение компонент
            mst.append((u, v, weight))  # Добавляем ребро в остовное дерево
            total_cost += weight  # Увеличиваем общую стоимость

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
