class Graph:
    """Класс графа для поиска точек сочленения"""
    def __init__(self, v_count):
        self.graph = [set() for _ in range(v_count)]
        self.tin = self.fup = self.timer = self.used = self.result = None
        self.reset_articulation_point_params()

    def reset_articulation_point_params(self):
        self.tin = [0] * self.v_count()
        self.fup = [0] * self.v_count()
        self.used = set()
        self.result = set()
        self.timer = 0

    def v_count(self):
        return len(self.graph)

    def add_edge(self, v1, v2):
        self.graph[v1].add(v2)
        self.graph[v2].add(v1)

    def dfs(self, curr_i, prev=None):
        self.used.add(curr_i)
        self.tin[curr_i] = self.fup[curr_i] = self.timer
        self.timer += 1
        children_count = 0
        for next_i in self.graph[curr_i]:
            if next_i is prev:
                continue
            if next_i not in self.used:
                children_count += 1
                self.dfs(next_i, curr_i)
                self.fup[curr_i] = min(self.fup[curr_i], self.fup[next_i])
                if self.fup[next_i] >= self.tin[curr_i] and prev is not None:
                    self.result.add(curr_i)
            else:
                self.fup[curr_i] = min(self.fup[curr_i], self.tin[next_i])
        if prev is None and children_count > 1:
            self.result.add(curr_i)

    def get_key_staff(self):
        self.reset_articulation_point_params()
        self.dfs(0)
        result = self.result
        self.reset_articulation_point_params()
        return list(result)


if __name__ == '__main__':
    v_count, edge_count = map(int, input().split())
    g = Graph(v_count)
    for i in range(edge_count):
        v1, v2 = map(int, input().split())
        g.add_edge(v1 - 1, v2 - 1)
    key_staff_list = g.get_key_staff()
    if key_staff_list:
        key_staff_list.sort()
        print(*(n + 1 for n in key_staff_list))
    else:
        print(-1)