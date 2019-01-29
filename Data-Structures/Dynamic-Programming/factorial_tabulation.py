def factorial_tabulation(n):

    fact = [1]

    for i in range(1, n+1):
        fact.append(fact[i-1] * i)

    print(fact)

if __name__ == "__main__":

    factorial_tabulation(10)
