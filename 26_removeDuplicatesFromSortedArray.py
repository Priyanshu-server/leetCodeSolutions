class Solution:
    def removeDuplicates(self, nums) -> int:
        n = len(nums)
        if(n==0 or n==1):
            return n
            
        j=1
        for i in range(1,n):

            if(nums[i]!=nums[i-1]):
                nums[j]=nums[i]
                #Logic is very simple i only make the array unique from front
                # as i get a unique value it will be changed at j index which is the point for our unique array
                j+=1
        return j,nums


sol  = Solution()
print(sol.removeDuplicates([1,2,2,3,3,4,5,5]))
