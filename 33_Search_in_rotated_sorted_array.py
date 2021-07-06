class Solution(object):
    def search(self, nums, target):
        low,high = 0,len(nums)-1
        while low<=high:

            mid  = (low+high+1)//2 #adding 1 bcz low is 0 so 0+index will not give the proper length
            if nums[mid] == target:
                return mid
            
            if nums[low] < nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1

sol = Solution()
# print(sol.search([4,5,6,7,0,1,2], 0))
# print(sol.search([4,5,6,7,0,1,2], 3))
print(sol.search([3,1], 3))