from queue import Queue
n, m = map(int, input().split())
# adj_list = [dict() for _ in range(n)]
adj_list_cong = [dict() for _ in range(n)]
max_flow = 0
for _ in range(m):
    u, v, c = map(int, input().split())
    # adj_list[u][v] = 0  # в норм такую сеть записываем
                             # потоки(через ребра на данной итерации)
    adj_list_cong[u][v] = c  # в дополняющую сеть записываем остаточные пропускные способности



def raise_flow_bfs(s, f):
    global max_flow
    visited = set()
    ochered = Queue()
    path = []
    rodnie_dushi = [None for _ in range(n)]

    for ver in adj_list_cong[s].keys():
        ochered.put(ver)
        rodnie_dushi[ver] = s
    visited.add(s)

    while not ochered.empty():
        cur = ochered.get()
        for ver in adj_list_cong[cur]:
            if ver not in visited:
                ochered.put(ver)
                rodnie_dushi[ver] = cur
        visited.add(cur)

    path.append(f)
    min_c = float('inf')
    while True:
        if path[-1] == s:
            break
        elif rodnie_dushi[path[-1]] is None:
            return max_flow
        else:
            if min_c > adj_list_cong[rodnie_dushi[path[-1]]][path[-1]]:
                min_c = adj_list_cong[rodnie_dushi[path[-1]]][path[-1]]
            path.append(rodnie_dushi[path[-1]])

    path = path[::-1]
    max_flow += min_c

    for i in range(len(path) - 1):
        adj_list_cong[path[i]][path[i + 1]] -= min_c
        # adj_list[path[i]][path[i + 1]] += min_c
        if adj_list_cong[path[i]][path[i + 1]] == 0:
            adj_list_cong[path[i]].pop(path[i + 1])

    return False


res = False
while not res:
    res = raise_flow_bfs(0, n - 1)
print(res)