
def more_than_neighbours(numbers):
    counter = 0
    if len(numbers) >= 3:
        for i in range(1, len(numbers) - 1):
            if numbers[i] > numbers[i - 1] and numbers[i] > numbers[i + 1]:
                counter += 1
    return counter


assert more_than_neighbours([1, 2, 3, 4, 5]) == 0
assert more_than_neighbours([5, 4, 3, 2, 1]) == 0
assert more_than_neighbours([1, 5, 1, 5, 1]) == 2
assert more_than_neighbours([1]) == 0
assert more_than_neighbours([1, 2]) == 0

def main():
    numbers = list(map(float, input().split()))
    answer = more_than_neighbours(numbers)
    print(answer)

if __name__ == '__main__':
    main()