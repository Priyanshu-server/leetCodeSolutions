class Solution:
    def intToRoman1(self,num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        result,i = "",0
        while num>0:
            result += (num//values[i])*numerals[i]
            num %= values[i]
            i+= 1
        return result

sol = Solution()
print(sol.intToRoman1(1009))