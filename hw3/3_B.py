def main():
    with open('input.txt', 'r') as f:
        main_set = None
        for line in f:
            if main_set is None:
                main_set = {int(x) for x in line.split()}
            else:
                main_set = main_set & {int(x) for x in line.split()}
    print(' '.join([str(x) for x in sorted(main_set)]))


if __name__ == '__main__':
    main()
