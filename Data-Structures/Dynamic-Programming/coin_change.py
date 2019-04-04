def coin_change_recursive(coins, n, result):
    if n < 0:
        return
    if n == 0:
        print(list(map(lambda x: int(x), result.split(",")[:-1])))
        return
    else:
        for coin in coins:
            coin_change_recursive(coins, n-coin, result+str(coin)+",")

if __name__ == "__main__":

    coins = [1, 2, 5, 10]
    N = 10
    coin_change_recursive(coins, N, "")