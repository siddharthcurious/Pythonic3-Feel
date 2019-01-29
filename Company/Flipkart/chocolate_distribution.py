# Given an array of n integers where each value represents number of chocolates in a packet.
# Each packet can have variable number of chocolates.
# There are m students, the task is to distribute chocolate packets such that:
#
#     1. Each student gets one packet.
#     2. The difference between the number of chocolates in packet with maximum chocolates and packet with minimum chocolates given to the students is minimum.

import sys
def chocolate_distribution(arr, m):
    arr.sort()
    start = 0
    last = m
    L = len(arr)
    min_diff = sys.maxsize
    result = []
    while last <= L:
        if min_diff > arr[last-1] - arr[start]:
            min_diff = arr[last-1] - arr[start]
            result = arr[start:last]
        start += 1
        last += 1

    return result

if __name__ == "__main__":

    arr = [12, 4, 7, 9, 2, 23, 25, 41, 30, 40, 28, 42, 30, 44, 48, 43, 50]
    m = 7
    r = chocolate_distribution(arr, m)
    print(r)
