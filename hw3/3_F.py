def compare_genomes(g1, g2):
    count_dict = {}
    for i in range(len(g1) - 1):
        pair = g1[i:i+2]
        if pair not in count_dict.keys():
            count_dict[pair] = 0
        if pair in count_dict.keys():
            count_dict[pair] += 1
    count = 0
    for i in range(len(g2) - 1):
        pair = g2[i:i + 2]
        if pair in count_dict.keys():
            count += count_dict[pair]
            del count_dict[pair]

    return count


def main():
    g1 = input()
    g2 = input()
    answ = compare_genomes(g1, g2)
    print(answ)


assert compare_genomes('ABBACAB', 'BCABB') == 4

if __name__ == '__main__':
    main()