import operator
def top_viewed_videos(videos, k):
    V = sorted(videos, key=operator.itemgetter(1), reverse=True)
    return V[:k]

if __name__ == "__main__":

    L = [("abc", 10), ("def", 15), ("ghi", 10), ("abc", 12), ("san", 20), ("hare", 30), ("xyz", 100), ("pqr", 50), ("pan", 60), ("mam", 90)]
    k = 4
    r = top_viewed_videos(L, k)
    print(r)