import heapq

def heapsort(iterables):

    heap = []
    for element in iterables:
        heapq.heappush(heap, element)

    return [heapq.heappop(heap)for i in range(len(heap))]

if __name__ == "__main__":

    numbers = [1, 4, 7, 9, 3, 6, 8, 10, 6, 12, 16, 17]
    numbers_sort = heapsort(numbers)
    print(numbers_sort)
