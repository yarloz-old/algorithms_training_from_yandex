def get_key_functionality(n_of_keys, durability, n_of_clicks, sequence_of_clicks):
    for key in sequence_of_clicks:
        durability[key - 1] -= 1

    return ["YES" if x < 0 else "NO" for x in durability]


def main():
    n_of_keys = int(input())
    durability = [int(x) for x in input().split()]
    n_of_clicks = int(input())
    sequence_of_clicks = [int(x) for x in input().split()]

    answer = get_key_functionality(n_of_keys, durability, n_of_clicks, sequence_of_clicks)
    print("\n".join(answer))


#assert get_key_functionality(5, [1, 50, 3, 4, 3], 16, [1, 2, 3, 4, 5, 1, 3, 3, 4, 5, 5, 5, 5, 5, 4, 5]) == ["YES", "NO", "NO", "NO", "YES"]


if __name__=="__main__":
    main()