import sys


def main():
    counts = {}
    count_line = []
    for line in sys.stdin:
        text = line.split()
        for word in text:
            if word in counts:
                count_line.append(counts[word])
                counts[word] += 1
            else:
                count_line.append(0)
                counts[word] = 1

    print(" ".join([str(x) for x in count_line]))


if __name__ == '__main__':
    main()