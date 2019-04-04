import heapq
def merge(lists):

    heap = []
    for lst in lists:
        if lst:
            heap.append(lst[0])
    heapq.heapify(heap)

    r = []
    c = 1
    L = len(lists[1])
    while heap:
        e = heapq.heappop(heap)
        r.append(e)



        heapq.heapify(heap)
    print(heap)
    print(r)





if __name__ == "__main__":

    LL = [[10, 15, 30], [12, 15, 20], [17, 20, 32]]
    r = merge(LL)
    print(r)