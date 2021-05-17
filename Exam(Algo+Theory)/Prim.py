n, m = map(int, input().split())

adj_list = [set() for _ in range(n)]

for _ in range(m):
    a, b, w = map(int, input().split())
    adj_list[a].add((b, w))
    adj_list[b].add((a, w))


visited = set()
visited.add(0)

def bfs():
    price = 0
    edges = []

    while len(visited) < n:
        min_w = float('inf')
        min_ver = None
        parent = None
        for v in visited:
            for u, w in adj_list[v]:
                if w < min_w and u not in visited:
                    min_w = w
                    min_ver = u
                    parent = v

        edges.append(list([parent, min_ver]))
        visited.add(min_ver)
        price += min_w

    print(price)
    for e in edges:
        print(*e)


bfs()