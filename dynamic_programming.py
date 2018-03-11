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




if __name__ == '__main__':
    unittest.main()
