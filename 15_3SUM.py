class Solution:
    def threeSum(self,nums):
        result = []
        nums.sort()
        for i, val in enumerate(nums):
            if i > 0 and val == nums[i - 1]:
                continue

            left_index = i + 1
            right_index = len(nums) - 1

            while left_index < right_index:
                sum = val + nums[left_index] + nums[right_index]

                if sum > 0:
                    right_index -= 1

                elif sum < 0:
                    left_index += 1
                else:

                    result.append([val, nums[left_index], nums[right_index]])
                    #No need to check if it is in result or not becuase we are getting out of that digit which means it is not going to comeback
                    left_index += 1
                    right_index -=1
                    
                    while nums[left_index]==nums[left_index-1] and left_index < right_index :
                        left_index +=1
                    while nums[right_index]==nums[right_index+1] and left_index < right_index :
                        right_index -= 1

        return result   

sol = Solution()
print(list(sol.threeSum([-1,0,1,2,-1,-4])))  #[[-1, 0, 1], [-1, -1, 2]]
print(sol.threeSum([-1,0,1,2,-1,-4,-2,-3,3,0,4]))
