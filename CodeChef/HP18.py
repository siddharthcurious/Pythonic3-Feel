def game(seq, N, b, a):
    bob = 0
    alice = 0
    c = 0



if __name__ == "__main__":

    T = int(input())
    for _ in range(T):
        N, a, b = [int(item) for item in input().split()]
        alice = b
        bob = a
        seq = [int(item) for item in input().split()]
        winner =  game(seq, N, bob, alice)