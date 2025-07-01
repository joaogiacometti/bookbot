def count_words(content):
    if not content:
        return 0
    return len(content.split())


def get_character_count(content):
    count_dict = {}

    for word in content.split():
        for char in word.lower():
            if char not in count_dict:
                count_dict[char] = 1
            else:
                count_dict[char] += 1
    return count_dict


def sort_on(items):
    return items["count"]


def get_most_common_characters(content, n=10):
    count_dict = get_character_count(content)

    count_list = []

    for char in count_dict:
        if char.isalpha():
            count_list.append({"char": char, "count": count_dict[char]})

    count_list.sort(reverse=True, key=sort_on)

    count_list = count_list[:n]

    return count_list
