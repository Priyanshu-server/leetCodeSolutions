class Solution(object):
    def letterCombinations(self, digits):
        mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        result = []
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return mapping[digits]

        for i,digit in enumerate(digits):
            if i == 0:
                result.extend(list(mapping[digit]))
            else:
                result = [prev_chars+curr_chars for prev_chars in result for curr_chars in mapping[digit]]
        return result
                
            

sol = Solution()
print(sol.letterCombinations("234"))





## Recusrsive Solution

# class Solution(object):
#     def letterCombinations(self, digits):
#         mapping = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
#             '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        
#         if len(digits) == 0:
#             return []
        
#         if len(digits) == 1:
#             return mapping[digits[0]]
        
#         prev = self.letterCombinations(digits[:-1])
#         additional = mapping[digits[-1]]
#         return [s + c for s in prev for c in additional]

# sol = Solution()
# print(sol.letterCombinations("23"))