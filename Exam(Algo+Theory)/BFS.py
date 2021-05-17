"""
--------------------------------------------------------------------
Описание: Алгоритм поиска в ширину

Пусть фиксирована начальная вершина s.

Алгоритм перечисляет все вершины достижимые из s
в порядке возрастания расстояния от s

Расстоянием считается кратчайшая длина кратчайшего пути(число рёбер)

В процессе поиска из графа выделяется дерево поиска в ширину

Алгоритм применим к ориентированным и неориентированным графам

--------------------------------------------------------------------
Реализация

Вершины могут иметь белый, серый и черный цвет

Граф хранится в списке смежности.
Для каждой вершины дополнительно хранятся её цвет и предок

В начале работы алгоритма все вершины белые. При заходе в новую вершину
она красится в серый цвет.

"""


#  Элемент односвязного списка
#  Используется для реализации очереди
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def __bool__(self):
        if self.first is None:
            return False
        return True

    def put(self, x):
        if self.first is None:
            self.first = self.last = Node(x, None)
        else:
            self.last.next = self.last = Node(x, None)

    def get(self):
        if self.first is None:
            return None
        else:
            res = self.first.value
            if self.last == self.first:
                self.first = self.last = None
            else:
                self.first = self.first.next

            return res


def bfs(s: int):
    color = [0 for _ in range(n)]
    ancestor = [None for _ in range(n)]
    distance = [float('inf') for _ in range(n)]

    distance[s] = 0

    q = Queue()
    q.put(s)

    while q:
        u = q.get()
        color[u] = 1
        for v in adj_list[u]:
            if color[v] == 0:
                color[v] = 1
                distance[v] = distance[u] + 1
                ancestor[v] = u
                q.put(v)
        color[u] = 2
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


if __name__ == '__main__':  # для неориентированного
    n, m = map(int, input().split())
    adj_list = dict()
    for i in range(n):
        adj_list[i] = set()
    for _ in range(m):  # граф задаётся списком рёбер
        a, b = map(int, input().split())
        adj_list[a].add(b)
        adj_list[b].add(a)

    res = bfs(0)
    print(res)
    print(*restore_path(0, 4, res['ancestor']))


"""
5 5
0 1
0 2
1 2
2 3
1 4
"""