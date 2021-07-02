class Solution(object):
    def myAtoi(self, s):
        s = s.strip()
        if len(s) == 0: return 0

        sign = 1
        if s[0] in ["-","+"]:
            sign = -1 if s[0] == "-" else 1
            s = s[1:]


        new_strng = ''
        
        for char in s:
            if 48<=ord(char)<=57 :
                new_strng = new_strng+char
            else:
                break

        if new_strng !="":

            bound  = pow(2,31)
            return max(-bound, min(sign * int(new_strng),bound-1))
        return 0

sol = Solution()
print(sol.myAtoi("   -42"))