import sys


def count_words():
    words_dict = set()
    for line in sys.stdin:
        words_dict.update(set(line.strip().split()))
    return len(words_dict)


def main():
    print(count_words())


if __name__ == '__main__':
    main()