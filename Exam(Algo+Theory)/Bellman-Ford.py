"""
--------------------------------------------------------------------
Описание: Алгоритм Беллмана-Форда

Решает задачу о кратчайших путях из одной вершины

Разрешает рёбра с отрицательным весом

Граф хранится в виде списка рёбер
--------------------------------------------------------------------

--------------------------------------------------------------------
"""


def relax(u, v, w):
    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w


def Bellman_Ford():
    for _ in range(n - 1):
        for u, v, w in edges:
            relax(u, v, w)

    for _ in range(2):
        for u, v, w in edges:
            if distance[v] > distance[u] + w:
                distance[v] = distance[u] + w
                neg_cycle.add(u)
                neg_cycle.add(v)

    dist = ['UDF' if (d == float('inf') or i in neg_cycle) else d for i, d in enumerate(distance)]


    print(*dist)


if __name__ == "__main__":
    n, m, s = map(int, input().split())
    edges = []
    for _ in range(m):
        edges.append(tuple(map(int, input().split())))
    distance = [float('inf') if i != s else 0 for i in range(n)]

    neg_cycle = set()