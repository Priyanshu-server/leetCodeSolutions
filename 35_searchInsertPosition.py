class Solution(object):
    def searchInsert(self, nums, target):
        for indx,item in enumerate(nums):
            if item==target or item>=target:
                return indx
        return len(nums)

sol  = Solution()
print(sol.searchInsert([1,3,5,6], 2))
        