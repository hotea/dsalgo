#!/usr/bin/env python
# encoding: utf-8
import unittest

class LongestIncreasingSubsequence(unittest.TestCase):
    """最长递增子序列
    """
    def lengthOfLIS(self, nums: int) -> int:
        """
        :type nums: List[int]
        :rtype: int

        question: https://leetcode.com/problems/longest-increasing-subsequence/description/
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

    def test_lis(self):
        self.assertEqual(self.lengthOfLIS([]), 0)
        self.assertEqual(self.lengthOfLIS([1]), 1)
        self.assertEqual(self.lengthOfLIS([1, 3, 2, 4]), 3)




if __name__ == '__main__':
    unittest.main()
