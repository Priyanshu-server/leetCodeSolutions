class Solution(object):
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] += nums[i-1]
        return max(nums)

sol = Solution()
print(sol.maxSubArray([5,4,-1,7,8]))