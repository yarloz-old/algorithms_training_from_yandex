def count_diff_numbers(ls):
    return len(set(ls))

def main():
    ls = [float(x) for x in input().split()]
    diff_number = count_diff_numbers(ls)
    print(diff_number)


assert count_diff_numbers([1, 2, 3, 2, 1]) == 3
assert count_diff_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == 10
assert count_diff_numbers([1, 2, 3, 4, 5, 1, 2, 1, 2, 7, 3]) == 6

if __name__ == '__main__':
    main()