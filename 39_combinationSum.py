
class Solution(object):
    def combinationSum(self, candidates, target):
        ret = []
        self.dfs(candidates, target, [], ret)
        return ret
    
    def dfs(self, nums, target, path, ret):
        
        if target < 0:
            return 
        if target == 0:
            ret.append(path)
            return 
        for i in range(len(nums)):
            self.dfs(nums[i:], target-nums[i], path+[nums[i]], ret) 
            #Basically i will not again using the same numbers so the solution will be from same numbers
            # i will use nums[i:] which means if nums[0:all] is finished then i will not use initial digit
            #again because it may cause the same pattern repative



sol = Solution()
print(sol.combinationSum([2,3,6,7],7))




'''
# Slow Solution

class Solution(object):
    def combinationSum(self, candidates, target):
        main_arr = []
        if target == 0:
            return main_arr

        if target<0:
            return None

        for num in candidates:
            remainder =  target-num

            remainderResult = self.combinationSum(candidates,remainder)
            if remainderResult != None:
                if remainderResult == []:
                    main_arr.append([num])
                else:
                    for lst in remainderResult:
                        lst.append(num)
                        lst = sorted(lst)
                        if lst not in main_arr:
                            main_arr.append(lst)


        if main_arr == []:
            return None
        return main_arr

            

        return main_arr
sol = Solution()
print(sol.combinationSum([2,3,6,7],7))

'''