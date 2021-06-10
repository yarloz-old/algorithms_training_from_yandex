def find_max_product(numbers):
    inf = 5e5 + 1
    max_1 = -inf
    max_2 = -inf
    max_3 = -inf

    max_neg_1 = -inf
    max_neg_2 = -inf
    max_neg_3 = -inf

    min_neg_1 = 1
    min_neg_2 = 1

    for i in range(len(numbers)):
        if numbers[i] > 0:
            if numbers[i] >= max_1:
                max_3 = max_2
                max_2 = max_1
                max_1 = numbers[i]
            elif max_2 <= numbers[i] < max_1:
                max_3 = max_2
                max_2 = numbers[i]
            elif max_3 < numbers[i] < max_2:
                max_3 = numbers[i]
        else:
            if numbers[i] >= max_neg_1:
                max_neg_3 = max_neg_2
                max_neg_2 = max_neg_1
                max_neg_1 = numbers[i]
            elif max_neg_2 <= numbers[i] < max_neg_1:
                max_neg_3 = max_neg_2
                max_neg_2 = numbers[i]
            elif max_neg_3 < numbers[i] < max_neg_2:
                max_neg_3 = numbers[i]

            if numbers[i] <= min_neg_1:
                min_neg_2 = min_neg_1
                min_neg_1 = numbers[i]
            elif min_neg_2 > numbers[i] > min_neg_1:
                min_neg_2 = numbers[i]

    max_products = {}

    if max_1 != -inf and max_2 != -inf and max_3 != -inf:
        max_products[max_1 * max_2 * max_3] = [max_1, max_2, max_3]
    if max_1 != -inf and min_neg_1 != 1 and min_neg_2 != 1:
        max_products[max_1 * min_neg_1 * min_neg_2] = [max_1, min_neg_1, min_neg_2]
    if max_1 != -inf and max_2 != -inf and min_neg_1 != 1:
        max_products[max_1 * max_2 * min_neg_1] = [max_1, max_2, min_neg_1]
    if max_neg_1 != -inf and max_neg_2 != -inf and max_neg_3 != -inf:
        max_products[max_neg_1 * max_neg_2 * max_neg_3] = [max_neg_1, max_neg_2, max_neg_3]

    if len(max_products) > 0:
        max_key = max(max_products.keys())
        return max_products[max_key]
    else:
        return

assert sorted(find_max_product([3, 5, 1, 7, 9, 0, 9, -3, 10])) == sorted([10, 9, 9])
assert sorted(find_max_product([-5, -30000, -12])) == sorted([-5, -12, -30000])
assert sorted(find_max_product([1, 2, 3])) == sorted([3, 2, 1])
assert sorted(find_max_product([-1, -2, -1, -1, -3, -5])) == sorted([-1, -1, -1])
assert sorted(find_max_product([-1, -2, 1, 1, -3, -5])) == sorted([1, -3, -5])
assert sorted(find_max_product([-5, 2, 1, 1, -5])) == sorted([-5, 2, -5])
assert sorted(find_max_product([-5, -2, 1])) == sorted([-5, -2, 1])
assert sorted(find_max_product([1, 0, 5])) == sorted([1, 0, 5])

def main():
    numbers = list(map(int, input().strip().split()))
    answer = find_max_product(numbers)
    print(" ".join(map(str, answer)))


if __name__ == '__main__':
    main()

