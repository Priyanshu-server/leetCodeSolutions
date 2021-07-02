def twoSum(nums,target):
    memo = {}
    for i in range(len(nums)):
        if (target - nums[i]) in memo:
            return [memo[target-nums[i]],i]
        memo[nums[i]] = i


print(twoSum([1,2,2,3],4))