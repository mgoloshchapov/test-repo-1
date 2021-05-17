def dfs(u):
    color[u] = 1
    for v in adj_list[u]:
        if color[v] == 0:
            res = dfs(u)
            if res == 'NO':
                return res
        elif color[u] == 1:
            return 'NO'
    color[v] = 2
    top_sort.append(v)
    return None


if __name__ == '__main__':
    n, m = map(int, input().split())
    adj_list = [set() for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        adj_list[a].add(b)

    color = [0 for _ in range(n)]
    top_sort = []

    for u in range(n):
        if color[u] == 0:
            res = dfs(u)
            if res == 'NO':
                print('NO')
                break
    else:
        print(*top_sort[::-1])

