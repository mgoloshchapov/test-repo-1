"""
--------------------------------------------------------------------
Описание: Алгоритм поиска в глубину

Алгоритм идёт по графу "вглубь", пока существуют непройденные
исходящие рёбра, и возврашается искать другой путь, если таких рёбер нет.

Алгоритм заканчивает работу, когда найдены все вершины,
достижимые из исходной.
--------------------------------------------------------------------
Реализация

Вершины могут иметь белый, серый или черный цвет.
Изначально все вершины белые.

При первом заходе в вершину её цвет меняется на серый.
Когда будут просмотрены все вершины, смежные с данной,
её цвет сменится на чёрный.

На выходе алгоритма мы получаем дерево поиска в глубину/
лес поиска в глубину(для нескольких компонент связности)/
путь между вершинами(при наличии такового)

Граф хранится в списке смежности

Для хранения обрабатываемых вершин используется стек

Алгоритм работает на ориентированных и неориентированных графах
"""
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next


class Stack:
    def __init__(self):
        self.last = None

    def __bool__(self):
        if self.last is None:
            return False
        return True

    def put(self, x):
        if self.last is None:
            self.last = Node(x, None)
        else:
            self.last = Node(x, self.last)

    def get(self):
        if self.last is None:
            return None
        else:
            res = self.last.value
            self.last = self.last.next

            return res


def dfs_visit(u, time):
    color[u] = 1
    d[u] = time
    time += 1
    for v in adj_list[u]:
        if color[v] == 0:
            ancestor[v] = u
            dfs_visit(v, time)
    color[u] = 2
    f[u] = time
    time += 1


def dfs():
    for u in range(n):
        time = 0  # метка времени
        if color[u] == 0:
            dfs_visit(u, time)

    return {'ancestor': ancestor,
            'd': d,
            'f': f}


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

    color = [0 for _ in range(n)]
    ancestor = [None for _ in range(n)]
    d = [None for _ in range(n)]  # хранит время начала обработки вершины
    f = [None for _ in range(n)]  # хранит время окончания обработки вершины

    res = dfs()
    print(restore_path(0, 7, res['ancestor']))

"""
9 10
0 1
0 2
1 2
1 4
2 3
3 5
5 6
6 8
8 7
7 5
"""