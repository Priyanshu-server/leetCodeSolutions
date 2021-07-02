class Solution(object):
    def removeElement(self, nums, val):
        len_arr = 0
        for item in nums:
            if item !=val:
                nums[len_arr] = item
                len_arr += 1
        return len_arr,nums

sol = Solution()
print(sol.removeElement(nums = [3,2,2,3], val = 3))