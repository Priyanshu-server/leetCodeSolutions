class Solution(object):
    def maxArea(self, height):

        MAX = 0
        j = len(height)-1
        i = 0
        while i!=j:
            if height[i]>height[j]:
                area = min(height[i],height[j])*abs(i-j)
                j -=1
            else:
                area = min(height[i],height[j])*abs(i-j)
                i +=1
            MAX = max(MAX,area)
        return MAX

sol = Solution()
print(sol.maxArea([4,3,2,1,4]))