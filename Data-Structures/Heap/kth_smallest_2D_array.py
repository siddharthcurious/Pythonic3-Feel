import heapq

def kthSmallest(input, k):

    result = input[0]
    heapq.heapify(result)

    for row in input[1:]:
        for element in row:
            heapq.heappush(result, element)

    return heapq.nsmallest(k, result)[-1]

if __name__ == "__main__":
    input = [[10, 25, 20, 40],
           [15, 45, 35, 30],
           [24, 29, 37, 48],
           [32, 33, 39, 50]]
    k = 3
    r = kthSmallest(input, k)
    print(r)