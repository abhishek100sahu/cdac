class Solution:
    def __init__(self, num_list, target):
        self.num_list = num_list
        self.target = target

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]

obj = Solution(num_list=[2,7,11,15], target=9)
print(obj.twoSum(nums=[2,7,11,15], target=9))