
## need improvements  program is faster but not efficient

class Solution(object):
    def searchRange(self, nums, target):
        len_nums = len(nums)
        if len_nums == 1 and nums[0] == target:
            return [0,0]

        left,right = 0,len_nums-1
        
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                i,j = mid,mid
                while i != len_nums-1 and nums[i+1] == target:
                    i+=1
                while j!= 0 and nums[j-1] == target:
                    j-=1
                return [j,i]
            
            if nums[left] <=target < nums[mid]:
                right = mid-1
            else:
                left = mid+1
        return [-1,-1]
sol = Solution()
print((sol.searchRange([5,7,7,8,8,10],8)))

print((sol.searchRange([1,4],4)))




'''
#Nice Solution

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        low, high = 0, len(nums)-1
        first = self.findFirstIndex(nums, low, high, target)

        second = self.findLastIndex(nums, low, high, target)
        
        return [first, second]
    def findFirstIndex(self, nums, low, high, target):
        res = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                res = mid
                high = mid-1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return res
    
    def findLastIndex(self, nums, low, high, target):
        res = -1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                res = mid
                low = mid+1
            elif nums[mid] > target:
                high = mid-1
            else:
                low = mid + 1
        return res

'''