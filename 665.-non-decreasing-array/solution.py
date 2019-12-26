from typing import List
from testcase import testcase


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        copy = nums[:]
        if self.is_sorted(nums):
            return True
        for i, n in enumerate(nums):
            if i == len(nums) - 1:
                return False
            if n > nums[i + 1]:
                copy[i] = n - (n - nums[i + 1]) - 1
                if self.is_sorted(copy):
                    return True
                copy = nums[:]
                copy[i + 1] = n
                if self.is_sorted(copy):
                    return True
                return False
        return False

    def is_sorted(self, nums: List[int]) -> bool:
        return nums == sorted(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.checkPossibility(testcase))
