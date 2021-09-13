def main():
    n = int(input())
    blocks = {}
    for _ in range(n):
        w, h = [int(x) for x in input().split()]
        if w in blocks:
            if h > blocks[w]:
                blocks[w] = h
        else:
            blocks[w] = h

    print(sum(blocks.values()))


if __name__ == "__main__":
    main()
