import numpy as np


def function(m, ii, jj, kk):
    epsn = 1e5
    eps = 1e-5
    n = 0
    v = np.zeros([2000, 12])

    p = np.zeros((ii, jj, kk))
    for x in range(ii):
        counter = 0
        for z in range(kk):
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
        for a in range(jj):
            for b in range(kk):
                for item in np.nditer(p[x][a][b]):
                    if item == 1:
                        p[x][a][b] = total / counter
    c = np.ones((ii, jj, kk))

    while epsn > eps:
        n += 1
        for i in range(m-1):
            v[n][i] = 0
            for k in range(4):
                for j in range(m):
                    v[n][i] = v[n][i] + p[i][k][j]*(c[i][k][j] + v[n-1][j])
            e = 0
            for k in range(m):
                e = e + abs(v[n][k] - v[n-1][k])
            epsn = e

    print(v)


function(12, 12, 4, 12)


