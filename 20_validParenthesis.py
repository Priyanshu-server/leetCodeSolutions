class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dic = {')':'(','}':'{',']':'['}
        for char in s:
            if char in '({[':
                stack.append(char)
                continue
            if char in ')]}':
                if len(stack) > 0:
                    if stack[-1] != dic[char]:
                        return False
                    else:
                        stack.pop()
                        continue
                else:
                    return False
                    
        return True if len(stack) == 0 else False

sol= Solution()
print(sol.isValid("(]"))