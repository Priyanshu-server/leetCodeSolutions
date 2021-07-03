#Experiment File

class Solution(object):
    def divide(self, dividend, divisor):
        is_negative = (dividend<0) != (divisor<0)
        # i = 0
        # num = 0
        # while abs(num)<=abs(dividend):
        #     i+=1
        #     num += divisor

        # if dividend <0 and divisor <0:
        #     return i-1

        # elif dividend<0 or divisor<0:
        #     return -(i-1)
        # else:
        return is_negative

sol = Solution()
print(sol.divide(-0,-1))