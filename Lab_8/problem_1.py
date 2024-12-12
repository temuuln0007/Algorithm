import unittest

def coin_change(coins, amount):
    memo = {}

    def dp(rem):
        if rem in memo:
            return memo[rem]
        if rem == 0:
            return 0
        if rem < 0:
            return float('inf')
        
        min_coins = float('inf')
        for coin in coins:
            count = dp(rem - coin)
            print("count: ", count)
            min_coins = min(min_coins, count + 1)
        memo[rem] = min_coins
        return memo[rem]
    
    result = dp(amount)

    return result if result != float('inf') else -1

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
