from typing import List
from testcase import testcase


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        return self.single_pass_hash_map(nums, target)

    def brute_force(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            for j, m in enumerate(nums[i + 1 :]):
                if m + n == target:
                    return [i, j + i + 1]

    def two_pass_hash_map(self, nums: List[int], target: int) -> List[int]:
        h = dict()
        for i, n in enumerate(nums):
            h[n] = i

        for i, n in enumerate(nums):
            c = target - n
            index = h.get(c)
            if index and index != i:
                return [i, index]

    def single_pass_hash_map(self, nums: List[int], target: int) -> List[int]:
        h = dict()
        for i, n in enumerate(nums):
            index = h.get(target - n)
            if index is not None:
                return [index, i]
            h[n] = i


def test():
    s = Solution()
    for nums, target, expected in testcase:
        assert expected == s.brute_force(nums, target)
        assert expected == s.two_pass_hash_map(nums, target)
        assert expected == s.single_pass_hash_map(nums, target)


if __name__ == "__main__":
    s = Solution()
    for n, t, _ in testcase:
        print(s.twoSum(n, t))
