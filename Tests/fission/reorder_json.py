import operator

def reorder(input):
    if not input:
        return None
    if not isinstance(input, dict):
        return None

    indexes = input.get("indexes")
    output = {}
    if not indexes:
        return None
    if not isinstance(indexes, dict):
        return None
    else:
        indexes_sorted_on_keys = sorted(indexes.items(), key=operator.itemgetter(0))
        # indexes_sorted_on_keys = sorted(indexes.items(), key=lambda x: x[0]) # Sorted using lambda expression
        for key, value in indexes_sorted_on_keys:
            output.update({value: input.get(value)})

    return output

if __name__ == "__main__":

    input = {
        "k4": "value4",
        "k1": "v1",
        "k9": "value9",
        "k8": "value8",
        "k5": "value5",
        "k7": "value7",
        "k6": "dummyvalue",
        "k2": "value2",
        "k3": "value3",
        "k10": "any_value",
        "indexes": {
            "1": "k5",
            "7": "k8",
            "2": "k1",
            "8": "k3",
            "6": "k4",
            "0": "k2",
            "3": "k9",
            "4": "k6",
            "5": "k7",
            "9": "k10"
        }
    }

    r  = reorder(input)
    print(r)

