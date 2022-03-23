a = [
    [2, 2, 2, 2, 2, 2, 2, 2],
    [2, 1, 0, 0, 1, 0, 0, 2],
    [2, 1, 1, 0, 0, 0, 0, 2],
    [2, 0, 0, 0, 0, 1, 1, 2],
    [2, 0, 0, 0, 1, 1, 0, 2],
    [2, 2, 2, 2, 2, 2, 2, 2]
]

ni = 0


def explore(i, j):
    if a[i][j] == 1:
        a[i][j] = 0
        if a[i-1][j] == 1:
            explore(i - 1, j)
        if a[i-1][j+1] == 1:
            explore(i-1, j+1)
        if a[i][j+1] == 1:
            explore(i, j+1)
        if a[i+1][j+1] == 1:
            explore(i+1, j+1)
        if a[i+1][j] == 1:
            explore(i+1, j)
        if a[i+1][j-1] == 1:
            explore(i+1, j-1)
        if a[i][j-1] == 1:
            explore(i, j-1)
        if a[i-1][j-1] == 1:
            explore(i-1, j-1)


for i in range(1, len(a) - 1):
    for j in range(1, len(a[0]) - 1):
        if a[i][j] == 1:
            print(i, j)
            ni += 1
            explore(i, j)

print(ni)
