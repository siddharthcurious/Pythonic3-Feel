def compute_distinct_homonyms(secret_mapping, word_list):
    alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    dict_map = {}
    for k, v in zip(alph, secret_mapping):
        dict_map.update({k:v})

    result = set()
    for word in word_list:
        coded = ""
        for c in word:
            coded = coded + dict_map[c]
        result.add(coded)
    return len(result)


if __name__ == "__main__":


    compute_distinct_homonyms(secret_mapping, word_list)

