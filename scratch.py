import numpy as np


def generator(i, j, k):
    p = np.zeros((i, j, k))
    for x in range(i):
        counter = 0
        for z in range(k):
            total = 1
            left = False
            right = False
            up = False
            down = False
            if x - z == 1:
                counter += 1
                left = True
            if x - z == -1:
                counter += 1
                right = True
            if x - z == -4:
                counter += 1
                down = True
            if x - z == 4:
                counter += 1
                up = True
            if right:
                p[x][0][z] = 1
            if left:
                p[x][1][z] = 1
            if up:
                p[x][2][z] = 1
            if down:
                p[x][3][z] = 1
        for a in range(j):
            for b in range(k):
                for item in np.nditer(p[x][a][b]):
                    if item == 1:
                        p[x][a][b] = total/counter


def function(m):
    epsn = 1e5
    eps = 1e-5
    n = 0
    v = np.zeros([20, 4])

    p = [[0, 0.6, 0.4, 0],
         [0, 0, 0, 1],
         [0.3, 0, 0, 0.7]]

    c = [[0, 5, 2, 0],
         [0, 0, 0, 1],
         [3, 0, 0, 4]]

    while epsn > eps:
        n += 1

        for i in range(m-1):
            v[n][i] = 0
            for j in range(m):
                v[n][i] = v[n][i] + p[i][j]*(c[i][j] + v[n-1][j])
            e = 0
            for k in range(m):
                e = e + abs(v[n][k] - v[n-1][k])
            epsn = e

    print(v)


function(4)


