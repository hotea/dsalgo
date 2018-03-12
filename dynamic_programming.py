#!/usr/bin/env python
# encoding: utf-8
import unittest
from typing import List


class LongestIncreasingSubsequence(unittest.TestCase):
    """最长递增子序列
    question: https://leetcode.com/problems/longest-increasing-subsequence/description/
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int

        explaination: https://www.youtube.com/watch?v=CE2b_-XfVDk
        """
        if not nums:
            return 0
        result = [1] * len(nums)
        for i, i_elem in enumerate(nums[1:]):
            for j, j_elem in enumerate(nums[:i]):
                if j_elem < i_elem:
                    result[i] = max(result[i], result[j]+1)
        return max(result)

    def lengthOfLIS1(self, nums):
        """O(logn) time complexity
        reference: https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
        """
        if not nums:
            return 0
        tailtable = [0] * len(nums)
        tailtable[0] = nums[0]
        tail_index = 0
        for i in range(1, len(nums)):
            if nums[i] > tailtable[tail_index]:
                tailtable[tail_index+1] = nums[i]
                tail_index += 1
            else:
                l = 0
                r = tail_index 
                while l < r:
                    m = (l + r) // 2
                    if tailtable[m] < nums[i]:
                        l = m + 1
                    else:
                        r = m
                tailtable[l] = nums[i]
            print(tailtable)
            print(tail_index)
        return tail_index + 1

    def test_lis(self):
        self.assertEqual(self.lengthOfLIS([]), 0)
        self.assertEqual(self.lengthOfLIS([1]), 1)
        self.assertEqual(self.lengthOfLIS([1, 3, 2, 4]), 3)

    def test_lis1(self):
        self.assertEqual(self.lengthOfLIS1([]), 0)
        self.assertEqual(self.lengthOfLIS1([1]), 1)
        self.assertEqual(self.lengthOfLIS1([1, 3, 2, 4]), 3)
        self.assertEqual(self.lengthOfLIS1([10,9,2,5,3,7,101,18]), 4)


class CoinChange(unittest.TestCase):
    """兑换零钱最少需要的硬币数量，相同面值硬币可重复使用
    https://leetcode.com/problems/coin-change/description/
    """
    def coin_change(self, coins: List[int], amount: int) -> int:
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        MAX = float('inf')
        dp = [0] + [MAX] * amount
        for i in range(1, amount+1):
            for denomination in coins:
                if i >= denomination:
                    dp[i] = min(dp[i], dp[i-denomination]+1)
        return [dp[-1], -1][dp[-1] == MAX]

    def test_coin_change(self):
        self.assertEqual(self.coin_change([1, 2, 5], 11), 3)
        self.assertEqual(self.coin_change([2], 3), -1)




if __name__ == '__main__':
    # unittest.main()
    suite = unittest.TestSuite()

    tests_lis = [LongestIncreasingSubsequence("test_lis")]
    tests_lis1 = [LongestIncreasingSubsequence("test_lis1")]
    tests_coin_change = [CoinChange("test_coin_change")]

    # suite.addTests(tests_lis)
    # suite.addTests(tests_lis1)
    suite.addTests(tests_coin_change)


    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
