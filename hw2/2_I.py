def sapper(n, m, k, coordinates):
    field = [[0] * m for _ in range(n)]

    for i, j in coordinates:
        field[i - 1][j - 1] = "*"
    if k == 0 or k == n * m:
        return field

    for i in range(n):
        for j in range(m):
            if field[i][j] != "*":
                for g in range(max(0, i - 1), min(n, i + 2)):
                    for h in range(max(0, j - 1), min(m, j + 2)):
                        if field[g][h] == "*":
                            field[i][j] += 1
    return field


assert sapper(3, 2, 2, [[1, 1], [2, 2]]) == [["*", 2], [2, "*"], [1, 1]]
assert sapper(2, 2, 0, []) == [[0, 0], [0, 0]]
assert sapper(4, 4, 4, [[1, 3], [2, 1], [4, 2], [4, 4]]) == [[1, 2, "*", 1], ["*", 2, 1, 1],
                                                            [2, 2, 2, 1], [1, "*", 2, "*"]]


def main():
    n, m, k = map(int, input().split())
    coordinates = []
    for _ in range(k):
        coordinates.append(list(map(int, input().split())))
    answer = sapper(n, m, k, coordinates)
    print("\n".join([" ".join(map(str, x)) for x in answer]))


if __name__ == '__main__':
    main()
