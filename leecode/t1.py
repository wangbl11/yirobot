from _ast import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = len(nums)
        for i in range(0, cnt):
            for j in range(i + 1, cnt):
                if nums[i] + nums[j] == target:
                    return [i, j]

    def func2(self, nums: List[int], target: int) -> List[int]:
        pass


# sulotion = Solution()
# print(sulotion.twoSum([1, 4, 6, 10], 16))
