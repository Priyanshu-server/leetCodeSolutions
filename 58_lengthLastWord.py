class Solution(object):
    def lengthOfLastWord(self, s):
        return len(s.split()[-1]) if len(s.strip()) > 0 else 0


sol = Solution()
print(sol.lengthOfLastWord("Hello World"))