def countCoins(coins: str):
    coinCount = [0,0,0,0]
    for coin in coins:
        if (coin == 'p'):
            coinCount[3] += 1
        elif (coin == 'n'):
            coinCount[2] += 1
        elif (coin == 'd'):
            coinCount[1] += 1
        elif (coin == 'q'):
            coinCount[0] += 1
    return (coinCount[0], coinCount[1], coinCount[2], coinCount[3])

def getTotal(coinCount: tuple):
    total = 0.00
    total += coinCount[0] * 0.25
    total += coinCount[1] * 0.10
    total += coinCount[2] * 0.05
    total += coinCount[3] * 0.01
    return total

def main():
    running = True
    while (running):
        print("Enter a string of coins (x to quit): ", end="")
        coins = input().lower()
        if (coins[0] == 'x'): running = False
        else: 
            coinCount = countCoins(coins)
            print(f"Coin Count (Q, D, N, P): {coinCount}")
            print(f"Total monetary value: ${getTotal(coinCount):.2f}")

if __name__ == "__main__":
    main()