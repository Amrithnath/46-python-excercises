def find_longest_anagram_group(word_list: list) -> list:
    all_words = word_list.copy()
    sorted_words = [sorted(_.lower()) for _ in all_words]

    longest_group = []
    longest_group_len = 0

    while len(all_words):
        current_group = [all_words.pop(0)]
        sorted_base_word = sorted_words.pop(0)
        for idx, compare_word in enumerate(all_words):
            if sorted_base_word == sorted_words[idx]:
                all_words.pop(idx)
                sorted_words.pop(idx)
                current_group.append(compare_word)

        if len(current_group) > longest_group_len:
            longest_group_len = len(current_group)
            longest_group = [current_group]
        elif len(current_group) == longest_group_len:
            longest_group.append(current_group)

    return longest_group
