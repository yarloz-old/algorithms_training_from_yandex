
def triangle(first_freq, freqs):
    prev_freq = first_freq
    left_border = 30
    right_border = 4000
    for freq, direction in freqs:
        freq = float(freq)
        new_border = min(prev_freq, freq) + abs(freq - prev_freq) / 2
        if direction == "closer" and prev_freq < freq or direction == "further" and prev_freq > freq:
            left_border = new_border if new_border > left_border else left_border
        elif direction == "closer" and prev_freq > freq or direction == "further" and prev_freq < freq:
            right_border = new_border if new_border < right_border else right_border
        prev_freq = freq
    print([round(left_border, 6), round(right_border, 6)])
    return [round(left_border, 6), round(right_border, 6)]


assert triangle(440, [[220, "closer"], [300, "further"]]) == [30.0, 260.0]
assert triangle(554, [[880, "further"], [440, "closer"], [622, "closer"]]) == [531.0, 660.0]
assert triangle(30, [[30, "further"], [30, "closer"]]) == [30.0, 4000.0]
assert triangle(30, [[30, "closer"], [30, "further"]]) == [30.0, 4000.0]
assert triangle(30, [[30, "closer"], [30, "closer"]]) == [30.0, 4000.0]
assert triangle(30, [[30, "closer"], [4000, "further"]]) == [30.0, (4000 - 30)/2 + 30]

def main():
    n = int(input())
    first_freq = float(input())
    freqs = []
    for _ in range(1, n):
        freqs.append(input().split())

    answer = triangle(first_freq, freqs)
    print(" ".join(map(str, answer)))


if __name__ == '__main__':
    main()