class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        nums_len = len(nums)
        list = []

        for i in range(nums_len-1):
            for j in range(i+1, nums_len):
                if nums[i] + nums[j] == target:
                    return [i,j]
                     
