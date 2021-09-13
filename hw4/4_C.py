import sys


def most_frequent_word(lines):
    words_dict = {}

    for line in lines:
        text = line.split()
        for word in text:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1

    max_val = 0
    words = []
    for items in words_dict.items():
        if items[1] == max_val:
            words.append(items[0])
        elif items[1] > max_val:
            max_val = items[1]
            words = [items[0]]
    return sorted(words)[0]


def main():
    lines = []
    for line in sys.stdin:
        lines.append(line)
    answer = most_frequent_word(lines)
    print(answer)


#assert most_frequent_word(['apple orange banana banana orange']) == 'banana'
#assert most_frequent_word(['oh you touch my tralala mmm my ding ding dong']) == 'ding'
#assert most_frequent_word(['q w e r t y u i o p', 'a s d f g h j k l', 'z x c v b n m']) == 'a'


if __name__ == '__main__':
    main()