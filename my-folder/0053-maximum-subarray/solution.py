class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sub = nums[0]
        current_sum = 0

        for num in nums:
            current_sum += num
            
            if current_sum > max_sub:
                max_sub = current_sum
                
            # If current sum drops below 0, reset it
            if current_sum < 0:
                current_sum = 0

        return max_sub
            




