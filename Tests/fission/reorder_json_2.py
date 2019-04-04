import operator
from collections import OrderedDict
class Reorder:
    def reorder(self, input, indices):
        if not input:
            return None
        if not isinstance(input, dict):
            return None

        indexes = input.get(indices)
        if not indexes:
            return None
        if not isinstance(indexes, dict):
            return None
        else:
            data = []
            for key, value in indexes.items():
                data.append((key, (value, input.get(value))))
            sorted_data = sorted(data, key=operator.itemgetter(0))
            output = dict(OrderedDict([ item[1] for item in sorted_data]))
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

    obj = Reorder()
    actual_output  = obj.reorder(input, "indexes")

    expected = {
        "k2": "value2",
        "k5": "value5",
        "k1": "v1",
        "k9": "value9",
        "k6": "dummyvalue",
        "k7": "value7",
        "k4": "value4",
        "k8": "value8",
        "k3": "value3",
        "k10": "any_value",
    }


    print(actual_output)

    cmp_keys1 = expected.keys() - actual_output.keys()
    cmp_keys2 = expected.keys() - actual_output.keys()
    if not cmp_keys1 and not cmp_keys2:
        print("Pass - keys are matching")
    else:
        print("Failed - keys are not matching")

    flag = True
    for e_key, e_val, a_key, a_val in zip(expected.keys(), expected.values(), actual_output.keys(), actual_output.values()):
        if e_key != a_key or e_val != a_val:
            print("Faliled - order and keys values mismatch")
            flag = False
            break
    if flag == True:
        print("Pass - order and keys values matching")










