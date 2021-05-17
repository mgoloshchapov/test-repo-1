"""
--------------------------------------------------------------------
Описание: Алгоритм Дейкстры

Решает задачу о кратчайших путях из одной вершины для взвешенного
ориентированного графа с исходной вершиной s

Веса всех рёбер должны быть неотрицательны
--------------------------------------------------------------------
Реализация

Граф задан списком смежных вершин

Алгоритм выполняется, пока в куче heap есть пары (d, v), где
d = distance[v], v - вершина

На каждом шаге алгоритм извлекает минимум из heap, запускает релаксацию.
Если в процессе релаксации значение distance[v] поменялось,
то пара (d, v) удаляется из кучи и добавляется в её начало, после чего
элемент просеивается вниз

Релаксация ребра (u, v) состоит в следующем: значение distance[v]
уменьшается до distance[u] + w(u, v), если distance[v] > distance[u] + w(u, v).
Если distance[v] поменялось, то ancestor[v] = u
--------------------------------------------------------------------
"""


def sift_up(heap, i):
    while i > 0 and distance[heap[(i - 1) // 2]] > distance[heap[i]]:
        v2h[heap[i]], v2h[heap[(i - 1) // 2]] = (i - 1) // 2, i
        heap[i], heap[(i - 1) // 2] = heap[(i - 1) // 2], heap[i]
        i = (i - 1) // 2


def sift_down(heap, i):
    n = len(heap)
    while i * 2 + 1 < n:
        j = i
        if distance[heap[i]] > distance[heap[i * 2 + 1]]:
            j = i * 2 + 1
        if i * 2 + 2 < n and distance[heap[j]] > distance[heap[i * 2 + 2]]:
            j = i * 2 + 2
        if i == j:
            break
        v2h[heap[i]], v2h[heap[j]] = j, i
        heap[i], heap[j] = heap[j], heap[i]
        i = j


def add(heap, x):
    heap.append(x)
    sift_up(heap, len(heap) - 1)


def extract_min(heap):
    x = heap[0]
    heap[0] = heap.pop()
    v2h[heap[0]] = 0
    sift_down(heap, 0)
    return x


def relax(u, v, w):
    if distance[v] > distance[u] + w:
        distance[v] = distance[u] + w
        ancestor[v] = u
        sift_up(heap, v2h[v])


def Diikstra(s):
    while heap:
        u = extract_min(heap)
        if distance[u] == float('inf'):
            break
        for v, w in adj_list[u]:
            relax(u, v, w)

    return {'distance': distance,
            'ancestor': ancestor}


def restore_path(s, f, ancestor):
    path = [f]
    cur = f
    while True:
        prev = ancestor[cur]
        if prev == s:
            path.append(s)
            return path[::-1]

        elif prev is None:
            return -1
        else:
            cur = prev
            path.append(prev)


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj_list = {i: set() for i in range(n)}
    for _ in range(m):
        a, b, w = map(int, input().split())
        adj_list[a].add((b, w))

    # ввод начальной вершины
    s = int(input())

    # инициализация массива расстояний, предков
    distance = [float('inf') if i != s else 0 for i in range(n)]
    ancestor = [None for _ in range(n)]

    # инициализация кучи
    heap = [s] + [i for i in range(n) if i != s]

    # соответствие между индексами кучи и номерами вершин
    v2h = [i for i in range(n)]
    v2h[s], v2h[0] = 0, s

    res = Diikstra(s)
    print(res['distance'])
    print(restore_path(s, 0, res['ancestor']))

"""
5 6
4 0 3
4 1 7
0 1 1
3 1 4
1 2 2
2 3 3
1
"""