def main():
    n = int(input())
    vals = []
    for _ in range(n):
        a, b = [int(x) for x in input().split()]
        if a >= 0 and b >= 0:
            if a + b == n - 1:
                vals.append((a, b))

    print(len(set(vals)))


if __name__ == '__main__':
    main()