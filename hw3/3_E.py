def open_calculator(n, numbers):
    n_set = {int(x) for x in set(n)}
    return len(n_set - numbers)

def main():
    numbers = {int(x) for x in input().split()}
    n = input()
    answ = open_calculator(n, numbers)
    print(answ)

assert open_calculator('1123', {1, 2, 3}) == 0
assert open_calculator('1001', {1, 2, 3}) == 1
assert open_calculator('123', {5, 7, 3}) == 2


if __name__ == '__main__':
    main()