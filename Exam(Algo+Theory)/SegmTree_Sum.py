n = int(input())
nums = list(map(int, input().split()))
m = int(input())

pref = [nums[0]]
for i in range(1, n):
    pref += [pref[-1] + nums[i]]

req = []
for i in range(m):
    a, b = map(int, input().split())
    if a == 0:
        req += [pref[b]]
    elif b == 0:
        req += [0]
    else:
        req += [pref[b] - pref[a-1]]
print(*req)