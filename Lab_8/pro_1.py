import unittest

def coin_change(coins, amount):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    print(dp)

    for i in range(1, amount + 1):
        for coin in coins:
            if i - coin >= 0:  
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[amount] if dp[amount] != float('inf') else -1

coins = [1, 2, 5]
amount = 11
print(coin_change(coins, amount))

class TestCoinChange(unittest.TestCase):
    def test_example_case(self):
        coins = [1, 2, 5]
        amount = 11
        self.assertEqual(coin_change(coins, amount), 3)  # Жишээ тест

    def test_no_solution(self):
        coins = [2]
        amount = 3
        self.assertEqual(coin_change(coins, amount), -1)  # Боломжгүй тохиолдол

    def test_zero_amount(self):
        coins = [1, 2, 5]
        amount = 0
        self.assertEqual(coin_change(coins, amount), 0)  # 0 мөнгө, 0 зоос

    def test_single_coin(self):
        coins = [5]
        amount = 10
        self.assertEqual(coin_change(coins, amount), 2)  # Зөвхөн нэг төрлийн зоос

    def test_large_amount(self):
        coins = [1, 2, 5]
        amount = 100
        self.assertEqual(coin_change(coins, amount), 20)  # Том хэмжээтэй мөнгө

unittest.main()
