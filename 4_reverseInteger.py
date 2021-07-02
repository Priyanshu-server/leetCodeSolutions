class Solution(object):
    def reverse(self, x):
        is_negative = False    
        if x<0:
            x = -x
            is_negative = True

        reversed_int = 0
        while x>0:
            remainder = x%10
            reversed_int =  (reversed_int*10)+remainder
            x = x//10
        if is_negative:
            reversed_int = -reversed_int
        
        rng = pow(2,31)
        if reversed_int<-rng or reversed_int>rng:
            return 0
        return reversed_int
        

sol = Solution()
print(sol.reverse(1534236469))