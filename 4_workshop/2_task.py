from collections import deque

mat = [
    [0, 0, 0],
    [0, 1, 0],
    [1, 1, 1]
]

m = len(mat)
n = len(mat[0])
ans = [[float('inf')] * n for _ in range(m)]
queue = deque()

for i in range(m):
    for j in range(n):
        if mat[i][j] == 0:
            ans[i][j] = 0
            queue.append((i, j))

dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
while queue:
    i, j = queue.popleft()
    for di, dj in dirs:
        ni = i + di
        nj = j + dj
        if 0 <= ni < m and 0 <= nj < n:
            if ans[ni][nj] > ans[i][j] + 1:
                ans[ni][nj] = ans[i][j] + 1
                queue.append((ni, nj))

for row in ans:
    print(row)