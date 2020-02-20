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


    print(p)


generator(12, 4, 12)
