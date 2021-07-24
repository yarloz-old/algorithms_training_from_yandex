def number_of_shots(vals):
    n_of_shots = len({x[0] for x in vals})
    return n_of_shots

def main():
    n = int(input())
    vals = []
    for _ in range(n):
        x, y = [int(x) for x in input().split()]
        vals.append((x, y))
    answ = number_of_shots(vals)
    print(answ)


#assert number_of_shots([(1,1), (2, 2), (3, 3), (2, 1), (3, 2), (3, 1)]) == 3
#assert number_of_shots([(1,1), (2, 2), (3, 3), (2, 1), (3, 2), (3, 4)]) == 3


if __name__ == '__main__':
    main()