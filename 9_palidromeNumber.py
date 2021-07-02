class Solution:
    def isPalindrome(self, x: int) -> bool:
        intStr = str(x)

        if intStr[:] == intStr[::-1]:
            return True
        else:
            return False




sol = Solution()
print(sol.isPalindrome(121))