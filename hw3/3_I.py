def get_languages(all_sets):
    lang_all_know = set.intersection(*all_sets)
    lang_at_least_one = set.union(*all_sets)
    #print(len(lang_all_know))
    #print("\n".join(lang_all_know))
    #print(len(lang_at_least_one))
    #print("\n".join(lang_at_least_one))
    return len(lang_all_know), lang_all_know, len(lang_at_least_one), lang_at_least_one


def main():
    n = int(input())
    all_sets = []
    for _ in range(n):
        k = int(input())
        ind_set = set()
        for _ in range(k):
            ind_set.update({input()})
        all_sets.append(ind_set)
    all_know, lang_all_know, at_least_one, lang_at_least_one = get_languages(all_sets)
    print(all_know)
    print("\n".join(lang_all_know))
    print(at_least_one)
    print("\n".join(lang_at_least_one))


#assert get_languages([{"Russian", "English", "Japanese"}, {"Russian", "English"}, {"English"}]) == 3


if __name__ == '__main__':
    main()