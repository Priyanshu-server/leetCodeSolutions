class Solution:
    def romanToInt(self, s: str) -> int:
        roman_int_hash = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        integer = 0
        for i in range(len(s)):

            if i>0 and roman_int_hash[s[i-1]] < roman_int_hash[s[i]]:
                integer += (roman_int_hash[s[i]]-roman_int_hash[s[i-1]]*2)
                continue

            integer += roman_int_hash[s[i]]

        return integer
sol = Solution()
print(sol.romanToInt("IV"))
print(sol.romanToInt("III"))
print(sol.romanToInt("IX"))
print(sol.romanToInt("LVIII"))
print(sol.romanToInt("MCMXCIV"))