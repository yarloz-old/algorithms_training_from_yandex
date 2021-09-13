def main():
    N = int(input())
    d1 = {}
    d2 = {}
    for _ in range(N):
        key, value = input().split()
        d1[key] = value
        d2[value] = key
    query = input()
    if query in d1.keys():
        print(d1[query])
    elif query in d2.keys():
        print(d2[query])


if __name__ == '__main__':
    main()