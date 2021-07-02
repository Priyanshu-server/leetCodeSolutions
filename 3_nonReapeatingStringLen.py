# class Solution(object):
#     def lengthOfLongestSubstring(self, s):
#         a,b = 0,0
#         h_set = set()
#         Max = 0 
#         while b<len(s):
#             if s[b] not in h_set:
#                 h_set.add(s[b])
#                 Max = max(Max,len(h_set))
#                 b+=1
#             else:
#                 h_set.remove(s[a])
#                 a+=1

#         return Max

## best solution

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        h = {}
        Max = 0
        start = -1
        for index,word in enumerate(s):
            if word in h and h[word] >start:
                start = h[word]
            Max = max(Max, index - start)
            h[word] = index
        return Max

obj = Solution()
sol = obj.lengthOfLongestSubstring("pwweke")
print(sol)