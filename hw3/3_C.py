def cubes(set_ann, set_bor):
    return sorted(set_ann & set_bor), sorted(set_ann - set_bor), sorted(set_bor - set_ann)

def main():
    n, k = [int(x) for x in input().split()]
    set_ann = set()
    set_bor = set()
    for _ in range(n):
        set_ann.update({int(input())})
    for _ in range(k):
        set_bor.update({int(input())})

    set_common, set_only_ann, set_only_bor = cubes(set_ann, set_bor)
    print(len(set_common))
    print(' '.join([str(x) for x in set_common]))
    print(len(set_only_ann))
    print(' '.join([str(x) for x in set_only_ann]))
    print(len(set_only_bor))
    print(' '.join([str(x) for x in set_only_bor]))

#assert cubes({0, 1, 10, 9}, {1, 3, 0}) == ([0, 1], [9, 10], [3])
#assert cubes({1, 2}, {2, 3}) == ([2], [1], [3])
#assert cubes(set(), set()) == ([], [], [])


if __name__ == '__main__':
    main()